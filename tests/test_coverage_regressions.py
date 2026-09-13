import unittest
from commons.runner import run_agent
class CoverageRegressions(unittest.TestCase):
    def test_complementary_incompatible_candidates_are_not_full_coverage(self):
        payload={'problem_map':{'capabilities':[{'id':'sensor','component_type':'measurement','requirements':['detection'],'constraints':{'voltage':3.3,'outdoor':True}}]},
          'candidates':[{'id':'a','capability_id':'sensor','component_type':'measurement','classification':'prototype','source_ids':['s'],'requirements_met':['detection'],'constraint_fit':{'voltage':'met','outdoor':'unmet'}},
                        {'id':'b','capability_id':'sensor','component_type':'measurement','classification':'prototype','source_ids':['s'],'requirements_met':['detection'],'constraint_fit':{'voltage':'unmet','outdoor':'met'}}],
          'sources':[{'id':'s','passage':'Synthetic compatibility records'}]}
        result=run_agent('A3',payload)
        self.assertNotEqual(result['data']['gaps'][0]['status'],'provisionally_covered')
