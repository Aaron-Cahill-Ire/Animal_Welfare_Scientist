import unittest
from commons.runner import run_agent

class RunnerTests(unittest.TestCase):
    def test_unknown_agent(self):
        with self.assertRaises(ValueError):
            run_agent('ZZ', {})
    def test_budget_stop(self):
        r = run_agent('A2', {}, max_input_bytes=1)
        self.assertEqual(r['status'], 'abstained')
        self.assertIn('budget', r['required_action'])
    def test_private_input(self):
        r = run_agent('A2', {'data_classification':'restricted'})
        self.assertEqual(r['status'], 'abstained')
    def test_missing_input(self):
        r = run_agent('A2', {})
        self.assertEqual(r['status'], 'abstained')
        self.assertTrue(r['required_action'])

    def test_rejected_private_context_is_not_echoed(self):
        r = run_agent('A2', {'data_classification':'restricted','context':'private farm name'})
        self.assertNotIn('private farm name', str(r))
    def test_configuration_changes_with_limits(self):
        a=run_agent('A2', {})
        b=run_agent('A2', {},max_input_bytes=2)
        self.assertNotEqual(a['configuration_snapshot']['id'],b['configuration_snapshot']['id'])
