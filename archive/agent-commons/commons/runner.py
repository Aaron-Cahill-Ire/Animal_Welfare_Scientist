"""Public/synthetic, side-effect-free execution with content-addressed provenance."""
import hashlib
import json
import platform
import math
import signal
import threading
from contextlib import contextmanager
import time
import uuid
from copy import deepcopy
from pathlib import Path
from .registry import resolve
from .schema import validate, ValidationError

STATUSES = ['completed', 'partial', 'abstained', 'awaiting_human', 'awaiting_external', 'unsupported_input']


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def snapshot(agent_id, parameters=None):
    module, spec = resolve(agent_id)
    files = [Path(module.__file__), Path(__file__), Path(__file__).with_name('schema.py'), Path(__file__).with_name('registry.py')]
    code = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    manifest = {k: v for k, v in spec.items() if k != 'example'}
    version = digest({'code': code, 'manifest': manifest})
    config = {'agent_id': agent_id, 'agent_version': version,
              'backend': 'deterministic-python', 'model': None, 'prompt': None,
              'tools': [], 'dependencies': {'python': platform.python_version()},
              'permissions': [], 'parameters': parameters or {'input_bytes': 1000000, 'sources': 200, 'cost_usd': 0, 'runtime_seconds': 10}}
    return {**config, 'id': digest(config)}


def run_agent(agent_id, payload, *, max_input_bytes=1000000, max_sources=200, max_cost_usd=0, max_runtime_seconds=10):
    module, spec = resolve(agent_id)
    if not isinstance(payload, dict):
        raise ValidationError('Input must be a JSON object')
    if max_input_bytes < 1 or max_sources < 0 or max_cost_usd < 0 or max_runtime_seconds <= 0:
        raise ValueError('Budgets must be nonnegative and input/time limits positive')
    if not all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in (max_input_bytes, max_sources, max_cost_usd, max_runtime_seconds)):
        raise ValueError('Budgets must be finite numeric values')
    limits = {'input_bytes': max_input_bytes, 'sources': max_sources, 'cost_usd': max_cost_usd, 'runtime_seconds': max_runtime_seconds}
    config = snapshot(agent_id, limits)
    started = time.perf_counter()
    envelope = {'schema_version': '1.0', 'run_id': str(uuid.uuid4()), 'agent_id': agent_id,
                'agent_version': config['agent_version'], 'configuration_snapshot': config,
                'input_sha256': None, 'sources': [], 'runtime_seconds': 0.0, 'cost_usd': 0.0,
                'backend': config['backend'], 'human_review_required': True,
                'status': 'abstained', 'data': {}, 'warnings': [], 'required_action': None,
                'limitations': spec['limitations'], 'context': payload.get('context', 'Not specified') if payload.get('data_classification', 'synthetic') in ('public', 'synthetic') else 'Withheld',
                'data_classification': payload.get('data_classification', 'synthetic'),
                'limits': limits}
    try:
        if payload.get('data_classification', 'synthetic') not in ('public', 'synthetic'):
            raise ValidationError('Only explicitly public or synthetic inputs are supported; remove restricted data')
        encoded = canonical(payload).encode()
        if len(encoded) > max_input_bytes:
            raise ValidationError('Input budget exceeded; supply a smaller input or raise the input budget')
        validate(payload, {'type': 'object'})
        envelope['input_sha256'] = hashlib.sha256(encoded).hexdigest()
        sources = payload.get('sources', [])
        validate(sources, {'type': 'array', 'items': {'type': 'object', 'required': ['id'], 'properties': {'id': {'type': 'string', 'minLength': 1}}}})
        if len(sources) > max_sources:
            raise ValidationError('Source budget exceeded; reduce the approved collection')
        if len({s['id'] for s in sources}) != len(sources):
            raise ValidationError('Source IDs must be unique')
        envelope['sources'] = deepcopy(sources)
        validate(payload, {'type': 'object', 'required': spec['required']})
        validate(payload, spec['input_schema'])
        with _deadline(max_runtime_seconds):
            result = module.run(agent_id, deepcopy(payload))
        validate(result, {'type': 'object', 'required': ['status', 'data', 'warnings'], 'properties': {
            'status': {'enum': STATUSES}, 'data': {'type': 'object'}, 'warnings': {'type': 'array', 'items': {'type': 'string'}}}})
        validate(result['data'], spec['output_schema'])
        canonical(result)
        envelope.update({key: result[key] for key in ('status', 'data', 'warnings', 'required_action') if key in result})
    except (ValidationError, ValueError, TypeError, KeyError, IndexError, ZeroDivisionError, AttributeError, RecursionError, TimeoutError) as exc:
        envelope.update(status='abstained', data={}, required_action=str(exc), warnings=['Input or result could not be validated; no research conclusion was produced.'])
    envelope['runtime_seconds'] = round(time.perf_counter() - started, 6)
    if envelope['runtime_seconds'] > max_runtime_seconds:
        envelope.update(status='abstained', data={}, required_action='Runtime budget exceeded; reduce the input.', warnings=['Result discarded after exceeding runtime budget.'])
    return envelope


@contextmanager
def _deadline(seconds):
    # POSIX native CLI gets preemption; browser workers enforce their own hard cap.
    available = hasattr(signal, 'setitimer') and threading.current_thread() is threading.main_thread()
    if not available:
        yield
        return
    previous = signal.getsignal(signal.SIGALRM)
    def expired(signum, frame):
        raise TimeoutError('Runtime budget exceeded; reduce the input.')
    signal.signal(signal.SIGALRM, expired)
    old_timer = signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, *old_timer)
        signal.signal(signal.SIGALRM, previous)
