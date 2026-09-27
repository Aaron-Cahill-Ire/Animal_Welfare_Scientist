import unittest
from copy import deepcopy
from commons.registry import specs
from commons.workflows import start, resume, example

class WorkflowTests(unittest.TestCase):
    def approve(self,s,**kw):
        return resume(s,{'checkpoint_id':s['checkpoint_id'],'reviewer':'Synthetic test reviewer','approved':True,**kw})
    def test_discovery_preserves_capabilities_and_action_gap(self):
        s=start('discovery',example('discovery'))
        self.assertEqual(s['status'],'awaiting_human')
        self.assertEqual([r['agent_id'] for r in s['runs']],['A1','A2','A3','A6'])
        self.assertEqual(len(s['runs'][1]['data']['coverage']),3)
        self.assertEqual({x['component_type'] for x in s['runs'][0]['data']['capabilities']},{'causal','measurement','implementation'})
        gaps=s['runs'][2]['data']['gaps']
        self.assertTrue(any(g['capability_id']=='examination-access' and g['status']!='provisionally_covered' for g in gaps))
        self.assertEqual(self.approve(s)['status'],'completed')
    def test_approval_is_bound_and_explicit(self):
        s=start('hardware',example('hardware'))
        with self.assertRaises(ValueError): resume(s,{'reviewer':'x','approved':True})
        with self.assertRaises(ValueError): self.approve(s,approved='true')
        broken=deepcopy(s);broken['input']['criteria']=[]
        with self.assertRaises(ValueError): self.approve(broken)
        rejected=self.approve(s,approved=False)
        self.assertEqual(rejected['status'],'stopped')
    def test_hardware_requires_external_results_and_frozen_criteria(self):
        s=self.approve(start('hardware',example('hardware')))
        self.assertEqual(s['gate'],'bench_results')
        with self.assertRaises(ValueError): resume(s,{'checkpoint_id':s['checkpoint_id']})
        artifact={'checkpoint_id':s['checkpoint_id'],'results':[{'metric':'error','value':0.2,'unit':'C'}],'sources':[{'id':'bench','passage':'Synthetic measurement error 0.2 C.'}]}
        with self.assertRaises(ValueError): resume(s,{**artifact,'criteria':[]})
        r=resume(s,artifact)
        self.assertEqual(r['gate'],'final_review')
        self.assertEqual(r['runs'][-2]['data']['criteria'][0]['status'],'pass')
        self.assertTrue(any(x['id']=='bench' for x in r['runs'][-2]['sources']))
        self.assertEqual(self.approve(r)['status'],'completed')
    def test_intervention_preregisters_before_results(self):
        s=start('intervention',example('intervention'))
        self.assertEqual(s['gate'],'protocol_review')
        with self.assertRaises(ValueError): self.approve(s)
        pre=deepcopy(specs()['C3']['example'])
        pre['protocol'].update(population=s['input']['brief']['population'],outcomes=[s['input']['brief']['outcome']])
        s=self.approve(s,protocol=pre['protocol'],analysis_plan=pre['analysis_plan'])
        self.assertEqual(s['gate'],'registration')
        with self.assertRaises(ValueError): self.approve(s)
        s=self.approve(s,registration_reference='Synthetic registration (not submitted)')
        self.assertEqual(s['gate'],'study_results')
        s=resume(s,{'checkpoint_id':s['checkpoint_id'],'results':[{'metric':'error','value':0.2,'unit':'C'}],'sources':[{'id':'study','passage':'Synthetic measurements only'}],'rows':[{'reading':1},{'reading':3}],'columns':['reading']})
        self.assertEqual(s['gate'],'final_review')
        self.assertEqual(self.approve(s)['status'],'completed')
    def test_research_data_branch(self):
        p=example('research');p.update(rows=[{'x':1},{'x':3}],columns=['x'],data_dictionary={'x':{'type':'number'}})
        s=start('research',p)
        self.assertEqual(s['gate'],'final_review')
        self.assertEqual([r['agent_id'] for r in s['runs']],['C1','C6','A6','C2','B5','C5'])
    def test_private_workflow_rejected(self):
        with self.assertRaises(ValueError):start('hardware',{'data_classification':'restricted'})

    def test_discovery_no_candidates_still_returns_gap_report(self):
        p=example('discovery');p['sources']=[]
        state=start('discovery',p)
        self.assertEqual(state['status'],'awaiting_human')
        self.assertEqual(state['gate'],'final_review')
        self.assertTrue(state['runs'][2]['data']['gaps'])
