import unittest

from commons.agents import track_a


class TrackATests(unittest.TestCase):
    def test_semantic_benchmarks(self):
        cases = track_a.benchmark_cases()
        for agent_id in track_a.SPECS:
            self.assertGreaterEqual(sum(c['agent_id'] == agent_id for c in cases), 4)
        for case in cases:
            with self.subTest(case=case['id']):
                self.assertTrue(case['check'](track_a.run(case['agent_id'], case['input'])))

    def test_examples_and_baselines(self):
        for agent_id, spec in track_a.SPECS.items():
            with self.subTest(agent=agent_id):
                result = track_a.run(agent_id, spec['example'])
                self.assertIsInstance(result['data'], dict)
                self.assertIn(result['status'], ['completed', 'partial', 'abstained', 'awaiting_human'])
                baseline = track_a.baseline(agent_id, spec['example'])
                self.assertEqual(set(result['data']), set(baseline['data']))

    def test_stable_mapper_ids(self):
        payload = track_a.SPECS['A1']['example']
        self.assertEqual(track_a.run('A1', payload), track_a.run('A1', payload))

    def test_weighted_scoring(self):
        result = track_a.run('A4', {'candidates': [
            {'id': 'one', 'scores': {'benefit': 8, 'cost': 2}},
            {'id': 'two', 'scores': {'benefit': 5, 'cost': 0}}],
            'criteria': [{'id': 'benefit', 'weight': 3, 'min': 0, 'max': 10},
                         {'id': 'cost', 'weight': 1, 'min': 0, 'max': 10, 'direction': 'minimize'}]})
        self.assertEqual(result['data']['comparison'][0]['id'], 'one')
        self.assertAlmostEqual(result['data']['comparison'][0]['score'], .8)
        self.assertTrue(result['data']['human_review_required'])

    def test_output_is_not_mutated_input(self):
        import copy
        for agent_id, spec in track_a.SPECS.items():
            original = copy.deepcopy(spec['example'])
            track_a.run(agent_id, spec['example'])
            self.assertEqual(original, spec['example'])

    def test_missing_requirement_evidence_is_not_failure_evidence(self):
        result = track_a.run('A3', {
            'problem_map': {'capabilities': [{'id': 'action', 'component_type': 'implementation',
                                             'requirements': ['route an animal for examination']}]},
            'candidates': [], 'sources': []})
        gap = result['data']['gaps'][0]
        self.assertEqual(gap['status'], 'insufficient_evidence')
        self.assertEqual(gap['unmet_requirements'], [])
        self.assertEqual(gap['not_evidenced_requirements'], ['route an animal for examination'])
        self.assertTrue(gap['search_unresolved'])

    def test_nonfinite_score_is_not_ranked(self):
        result = track_a.run('A4', {'candidates': [{'id': 'x', 'scores': {'benefit': float('nan')}}],
                                   'criteria': [{'id': 'benefit'}]})
        self.assertEqual(result['data']['proposed_shortlist'], [])
        self.assertIsNone(result['data']['comparison'][0]['score'])

    def test_partial_context_is_unknown(self):
        result = track_a.run('A6', {'claims': [{'id': 'c', 'text': 'Measured gait', 'source_ids': ['s'],
                                               'context': {'species': 'cow', 'system': 'dairy'}}],
                                   'sources': [{'id': 's', 'passage': 'Measured gait', 'context': {'species': 'cow'}}]})
        self.assertEqual(result['data']['findings'][0]['assessments'][0]['scope'], 'unknown')

    def test_duplicate_capability_ids_are_flagged(self):
        result = track_a.run('A1', {'brief': 'Measure gait', 'components': [
            {'type': 'measurement', 'description': 'Measure gait', 'required_capabilities': [
                {'id': 'gait', 'description': 'Measure gait'}, {'id': 'gait', 'description': 'Measure gait again'}]}]})
        self.assertEqual(len(result['data']['search_targets']), 1)
        self.assertTrue(any('Duplicate capability' in q for q in result['data']['unresolved_questions']))


if __name__ == '__main__':
    unittest.main()
