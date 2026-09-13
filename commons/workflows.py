"""Explicit checkpoint handoffs; approval records attest decisions, never grant tool permissions."""
from copy import deepcopy
from datetime import datetime, timezone
from .registry import specs
from .runner import run_agent, digest, snapshot

NAMES = ('discovery', 'intervention', 'hardware', 'research')


def _seal(state):
    state.pop('checkpoint_id', None)
    state['checkpoint_id'] = digest(state)
    return state


def _gate(state, name, status, action):
    state.update(gate=name, status=status, required_action=action)
    return _seal(state)


def _run(state, aid, payload, *, allow_empty_audit=False):
    payload = deepcopy(payload)
    payload['data_classification'] = state['input'].get('data_classification', 'synthetic')
    payload.setdefault('sources', state['input'].get('sources', []))
    payload['upstream_run_ids'] = [r['run_id'] for r in state['runs']]
    result = run_agent(aid, payload)
    state['runs'].append(result)
    state['warnings'].extend(w for w in result['warnings'] if w not in state['warnings'])
    state['warnings'].extend(w for w in result['limitations'] if w not in state['warnings'])
    if result['status'] in ('abstained', 'unsupported_input') and not (allow_empty_audit and aid == 'A6' and payload.get('claims') == []):
        raise ValueError(aid + ' cannot continue: ' + str(result['required_action']))
    return result['data']


def _report(state):
    return _run(state, 'C5', {'artifacts': [{'id': r['run_id'], 'type': 'results', 'content': r['data'], 'source_ids': [s['id'] for s in r['sources']]} for r in state['runs']], 'run_records': deepcopy(state['runs'])})


def start(name, payload):
    if name not in NAMES:
        raise ValueError('Unknown workflow')
    if payload.get('data_classification', 'synthetic') not in ('public', 'synthetic'):
        raise ValueError('Workflows accept public/synthetic data only')
    state = {'schema_version': '1.0', 'workflow': name, 'input': deepcopy(payload), 'runs': [], 'decisions': [], 'warnings': ['No studies, procurement or external submissions are performed.'], 'created_at': datetime.now(timezone.utc).isoformat()}
    try:
        if name == 'discovery':
            mapped = _run(state, 'A1', payload)
            scouted = _run(state, 'A2', {'search_targets': mapped['search_targets']})
            _run(state, 'A3', {'problem_map': mapped, 'candidates': scouted['candidates'], 'coverage': scouted['coverage']})
            claims = [{'id': 'candidate-'+str(i), 'text': c.get('evidence_quote', c.get('name', 'Candidate match')), 'claim_type': 'quotation', 'source_ids': c.get('source_ids', [])} for i, c in enumerate(scouted['candidates'])]
            _run(state, 'A6', {'claims': claims}, allow_empty_audit=True)
            return _gate(state, 'final_review', 'awaiting_human', 'Supply an explicit reviewer decision for this checkpoint before using the discovery report.')
        if name == 'hardware':
            concept = _run(state, 'B6', payload)
            _run(state, 'B7', {'requirements': payload.get('component_requirements', {}), 'supplier_records': payload.get('supplier_records', []), 'as_of': payload.get('as_of')})
            state['predefined_criteria'] = deepcopy(payload.get('criteria', []))
            return _gate(state, 'concept_review', 'awaiting_human', 'Review concept, component constraints and predefined bench criteria. Approval does not authorise purchasing or animal use.')
        if name == 'intervention':
            hypotheses = _run(state, 'B1', {'brief': payload['brief']})
            protocol = _run(state, 'B2', {'hypothesis': {**payload['brief'], 'generated_hypotheses': hypotheses['hypotheses']}, 'framework': payload['framework']})
            planner = _run(state, 'B3', {'protocol': {**payload.get('design', {}), 'protocol_draft': protocol['protocol_draft']}, 'resources': payload['resources']})
            _run(state, 'C4', {'brief': {**payload.get('ethics_brief', {}), 'protocol_draft': protocol['protocol_draft'], 'planning_output': planner}})
            state['predefined_criteria'] = deepcopy(payload.get('criteria', []))
            return _gate(state, 'protocol_review', 'awaiting_human', 'Supply reviewed protocol and analysis_plan plus reviewer decision. Unresolved study decisions must be resolved by qualified humans.')
        synthesis = _run(state, 'C1', payload)
        included = synthesis['evidence_table']
        findings = [{'question': payload['question'], 'finding': e.get('reported_finding'), 'source_ids': e.get('source_ids', [])} for e in included if e.get('human_included')]
        _run(state, 'C6', {'scope': {'questions': payload.get('questions', [payload['question']])}, 'synthesis': {'findings': findings, 'search_coverage': {'complete_within_scope': False, 'description': 'Supplied documents only; no external search'}}})
        _run(state, 'A6', {'claims': [{'id': e['document_id'], 'text': e.get('reported_finding') or e['passage'], 'source_ids': e.get('source_ids', [])} for e in included]}, allow_empty_audit=True)
        if payload.get('rows') is not None:
            _run(state, 'C2', {'rows': payload['rows'], 'data_dictionary': payload.get('data_dictionary', {})})
            _run(state, 'B5', {'rows': payload['rows'], 'columns': payload.get('columns', []), 'question': payload['question']})
        if payload.get('video') is not None:
            _run(state, 'B4', {'video': payload['video']})
        _report(state)
        return _gate(state, 'final_review', 'awaiting_human', 'Review evidence, unresolved questions and missing reporting artefacts before using this output.')
    except (ValueError, KeyError, TypeError) as exc:
        return _gate(state, 'input_required', 'abstained', str(exc))


def resume(checkpoint, artifact):
    state = deepcopy(checkpoint)
    cid = state.pop('checkpoint_id', None)
    if not cid or digest(state) != cid:
        raise ValueError('Checkpoint integrity mismatch; use the original saved checkpoint')
    if artifact.get('checkpoint_id') != cid:
        raise ValueError('Decision/results must identify this checkpoint_id')
    if state['status'] not in ('awaiting_human', 'awaiting_external'):
        raise ValueError('This checkpoint is not resumable')
    if artifact.get('data_classification', 'synthetic') not in ('public', 'synthetic'):
        raise ValueError('Only public/synthetic resume artefacts are supported')
    for result in state['runs']:
        if result['configuration_snapshot']['id'] != snapshot(result['agent_id'])['id']:
            raise ValueError('Agent configuration changed; restart the workflow and re-review its outputs')
    gate = state['gate']
    if state['status'] == 'awaiting_human':
        if not isinstance(artifact.get('reviewer'), str) or not artifact['reviewer'].strip() or not isinstance(artifact.get('approved'), bool):
            raise ValueError('Supply reviewer and explicit boolean approved decision')
        if not artifact['approved']:
            state['decisions'].append(deepcopy(artifact))
            return _gate(state, 'rejected', 'stopped', 'Reviewer declined; revise inputs and start a new workflow')
    state['decisions'].append(deepcopy(artifact))
    if gate == 'final_review':
        return _gate(state, 'complete', 'completed', 'Human-reviewed record only; no deployment, experiment or procurement has occurred')
    if gate == 'concept_review':
        if not state.get('predefined_criteria'):
            raise ValueError('Define bench criteria in the initial input before approval or testing')
        return _gate(state, 'bench_results', 'awaiting_external', 'Supply actual bench results and their source records; the software cannot perform physical testing')
    if gate == 'protocol_review':
        protocol = deepcopy(artifact.get('protocol', {}))
        if protocol.get('human_reviewed') is not True or not artifact.get('analysis_plan'):
            raise ValueError('Supply human_reviewed protocol and analysis_plan, not just an approval flag')
        brief = state['input']['brief']
        if protocol.get('population') != brief.get('population') or brief.get('outcome') not in protocol.get('outcomes', []):
            raise ValueError('Reviewed protocol population/outcome must match the original brief; restart for a changed study')
        pre = _run(state, 'C3', {'protocol': protocol, 'analysis_plan': artifact['analysis_plan']})
        if pre.get('unresolved_decisions') or pre.get('inconsistencies'):
            return _gate(state, 'protocol_review', 'awaiting_human', 'Resolve preregistration checklist/inconsistencies in the reviewed protocol and analysis plan')
        return _gate(state, 'registration', 'awaiting_human', 'Preregister externally before confirmatory data collection; supply registration_reference and explicit reviewer attestation')
    if gate == 'registration':
        if not artifact.get('registration_reference'):
            raise ValueError('Supply the external registration reference before study-results stage')
        return _gate(state, 'study_results', 'awaiting_external', 'Conduct approved work externally; then supply public/synthetic results, sources and deviations')
    if gate in ('bench_results', 'study_results'):
        if not artifact.get('sources') or not artifact.get('results'):
            raise ValueError('Supply results and source records; missing measurements cannot be manufactured')
        if 'criteria' in artifact:
            raise ValueError('Criteria are frozen before testing; resume cannot replace them')
        state['input']['sources'] = _merge_sources(state['input'].get('sources', []), artifact['sources'])
        if gate == 'study_results':
            if not artifact.get('rows') or not artifact.get('columns'):
                raise ValueError('Supply rows and columns for statistical analysis')
            _run(state, 'B5', {'rows': artifact['rows'], 'columns': artifact['columns'], 'question': state['input']['brief']['outcome']})
        _run(state, 'B8', {'criteria': state['predefined_criteria'], 'results': artifact['results'], 'unexpected_outcomes': artifact.get('deviations', [])})
        _report(state)
        return _gate(state, 'final_review', 'awaiting_human', 'Review supplied-result evaluation and reporting limitations; no welfare benefit or permission is inferred')
    raise ValueError('Unknown workflow gate')


def _merge_sources(left, right):
    merged = {s['id']: s for s in left}
    for source in right:
        if source['id'] in merged and source != merged[source['id']]:
            raise ValueError('Conflicting source record for ' + source['id'])
        merged[source['id']] = source
    return list(merged.values())


def example(name):
    s = specs()
    if name == 'discovery':
        p = deepcopy(s['A1']['example'])
        p['brief'] = 'Lameness in dairy cows: prevent hoof damage, detect abnormal gait, and route animals for examination.'
        p['components'] += [
            {'id': 'causal-flooring', 'type': 'causal', 'description': 'Flooring may contribute to hoof damage', 'epistemic_status': 'hypothesis', 'required_capabilities': [{'id': 'hoof-prevention', 'description': 'Prevent hoof damage', 'requirements': ['prevent hoof damage']}]},
            {'id': 'implementation-exam', 'type': 'implementation', 'description': 'Detected animals may not receive timely examination', 'epistemic_status': 'hypothesis', 'required_capabilities': [{'id': 'examination-access', 'description': 'Route affected animals for examination', 'requirements': ['examination routing']}]}]
        return p
    if name == 'hardware':
        return {**deepcopy(s['B6']['example']), 'component_requirements': {'voltage': 3.3}, 'supplier_records': deepcopy(s['B7']['example']['supplier_records']), 'as_of': '2026-09-13', 'criteria': deepcopy(s['B8']['example']['criteria']), 'sources': deepcopy(s['B7']['example'].get('sources', []))}
    if name == 'intervention':
        return {**deepcopy(s['B1']['example']), 'framework': deepcopy(s['B2']['example']['framework']), 'resources': deepcopy(s['B3']['example']['resources']), 'design': deepcopy(s['B3']['example']['protocol']), 'criteria': deepcopy(s['B8']['example']['criteria']), 'ethics_brief': {'animals': 'None; synthetic enclosure example', 'intervention': 'Environmental measurement'}, 'sources': deepcopy(s['B2']['example'].get('sources', []))}
    return deepcopy(s['C1']['example'])
