"""Development rubric runs, with actual matched simple-baseline results."""
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from .registry import modules, specs, resolve
from .runner import run_agent, snapshot, digest


def evaluate():
    records = []
    for module in modules():
        for case in module.benchmark_cases():
            started = time.perf_counter()
            actual = run_agent(case['agent_id'], case['input'])
            error = None
            try:
                passed = bool(case['check'](actual))
            except Exception as exc:
                passed, error = False, type(exc).__name__ + ': ' + str(exc)
            baseline_started = time.perf_counter()
            try:
                baseline_result = module.baseline(case['agent_id'], case['input'])
                baseline_passed = bool(case['check'](baseline_result))
                baseline_error = None
            except Exception as exc:
                baseline_passed, baseline_error = False, type(exc).__name__ + ': ' + str(exc)
            records.append({'case_id': case['id'], 'agent_id': case['agent_id'], 'category': case['category'],
                            'input_sha256': digest(case['input']), 'passed': passed, 'error': error,
                            'status': actual['status'], 'warnings': actual['warnings'],
                            'baseline_passed': baseline_passed, 'baseline_error': baseline_error,
                            'runtime_seconds': actual['runtime_seconds'], 'baseline_runtime_seconds': round(time.perf_counter()-baseline_started, 6),
                            'cost_usd': actual['cost_usd'], 'configuration_snapshot_id': actual['configuration_snapshot']['id']})
    summaries = {}
    for aid, spec in specs().items():
        rows = [r for r in records if r['agent_id'] == aid]
        summaries[aid] = {'n': len(rows), 'passed': sum(r['passed'] for r in rows),
                          'baseline_passed': sum(r['baseline_passed'] for r in rows),
                          'baseline': spec['baseline'], 'configuration_snapshot': snapshot(aid),
                          'failures': [r for r in rows if not r['passed']],
                          'abstentions': sum(r['status'] == 'abstained' for r in rows),
                          'uncertainty': 'Purposive developer-authored development cases; no population estimate or scientific confidence interval.',
                          'maturity': 'Prototype' if rows and all(r['passed'] for r in rows) else 'Documented'}
    return {'schema_version': '1.0', 'suite_version': 'starter-0.1.0', 'dataset_version': 'synthetic-development-0.1.0',
            'evaluated_at': datetime.now(timezone.utc).isoformat(), 'grading': 'Automated semantic assertions written by implementation developers; not independent.',
            'scientific_validation': 'Not performed', 'summaries': summaries, 'cases': records}


def write_results(directory='benchmarks/results'):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    result = evaluate()
    (directory / 'starter.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    (directory / 'failures.json').write_text(json.dumps([r for r in result['cases'] if not r['passed']], indent=2) + '\n')
    return result
