import json
import unittest
from pathlib import Path
from commons.registry import specs
from commons.runner import run_agent
from commons.schema import validate
class CatalogueContractTests(unittest.TestCase):
    def test_all_twenty_real_examples_satisfy_run_schema(self):
        schema=json.loads(Path('schemas/run-result.json').read_text())
        self.assertEqual(len(specs()),20)
        for aid,spec in specs().items():
            with self.subTest(agent=aid):
                result=run_agent(aid,spec['example'])
                validate(result,schema)
                self.assertNotIn(result['status'],('abstained','unsupported_input'))
                self.assertTrue(result['data'])
    def test_recorded_external_snapshots_are_distinct(self):
        records=json.loads(Path('catalogue/external.json').read_text())
        self.assertEqual(len(records),5)
        self.assertEqual(len({r['repository'] for r in records}),5)
        for r in records:
            self.assertEqual(len(r['commit']),40)
            self.assertEqual(r['security'],'Unreviewed')
            self.assertIn('Not executed',r['evidence_review']['finding'])
