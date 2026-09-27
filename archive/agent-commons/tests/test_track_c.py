import copy
import unittest
from commons.agents import track_c


class TrackCTests(unittest.TestCase):
    def test_semantic_benchmarks(self):
        cases = track_c.benchmark_cases()
        for agent in track_c.SPECS:
            self.assertGreaterEqual(sum(c['agent_id'] == agent for c in cases), 4)
        for case in cases:
            with self.subTest(case=case['id']):
                self.assertTrue(case['check'](track_c.run(case['agent_id'], case['input'])))

    def test_examples_and_baselines_are_computed_and_do_not_mutate(self):
        for agent, spec in track_c.SPECS.items():
            original = copy.deepcopy(spec['example'])
            for handler in (track_c.run, track_c.baseline):
                result = handler(agent, spec['example'])
                self.assertIsInstance(result['data'], dict)
                self.assertIn(result['status'], ('completed', 'partial', 'awaiting_human'))
                self.assertEqual(original, spec['example'])

    def test_missingness_and_kappa_exact(self):
        result = track_c.run('C2', {'rows': [{'a': 'yes', 'b': 'yes'}, {'a': 'no', 'b': 'yes'},
                                           {'a': 'no', 'b': 'no'}, {'a': 'yes', 'b': 'no'}, {'a': None, 'b': ''}],
                                  'data_dictionary': {'a': {}, 'b': {}}, 'rater_columns': ['a', 'b']})['data']
        self.assertEqual(result['missingness']['a'], {'count': 1, 'fraction': .2})
        self.assertEqual(result['annotation_reliability'][0]['paired_n'], 4)
        self.assertEqual(result['annotation_reliability'][0]['cohen_kappa'], 0)

    def test_human_include_survives_no_lexical_match(self):
        result = track_c.run('C1', {'question': 'pig', 'documents': [{'id': 'd', 'passage': 'Relevant synonym', 'human_decision': 'include', 'source_ids': ['a']} ]})
        self.assertEqual(result['data']['screening'][0]['decision'], 'include')
        self.assertEqual(result['data']['evidence_table'][0]['source_ids'], ['a'])

    def test_reliability_no_pairs_is_unknown(self):
        result = track_c.run('C2', {'rows': [{'a': 'x'}, {'b': 'y'}], 'data_dictionary': {'a': {}, 'b': {}}, 'rater_columns': ['a', 'b']})
        self.assertIsNone(result['data']['annotation_reliability'][0]['agreement'])

    def test_preregistration_mismatched_outcome_and_invalid_sample(self):
        result = track_c.run('C3', {'protocol': {'human_reviewed': True, 'sample_size': -1, 'outcomes': ['movement']}, 'analysis_plan': {'primary_outcome': 'happiness'}})
        self.assertEqual(len(result['data']['inconsistencies']), 2)
        self.assertFalse(result['data']['submitted'])

    def test_reference_is_not_verified_artifact(self):
        result = track_c.run('C5', {'artifacts': [{'id': 'data', 'type': 'data', 'path': '/etc/passwd'}], 'run_records': []})
        self.assertIn('data', result['data']['missing_artifact_checklist'])
        self.assertIsNone(result['data']['manifest'][0]['sha256'])
        self.assertFalse(result['data']['reproduced_execution'])

    def test_synthesis_never_implies_global_absence(self):
        result = track_c.run('C6', {'scope': {'questions': ['fish question']}, 'synthesis': {'findings': [], 'search_coverage': {'complete_within_scope': True, 'description': 'One bounded dataset'}}})
        self.assertEqual(result['data']['research_questions'][0]['classification'], 'bounded_evidence_gap')
        self.assertFalse(result['data']['global_absence_claim'])


if __name__ == '__main__':
    unittest.main()
