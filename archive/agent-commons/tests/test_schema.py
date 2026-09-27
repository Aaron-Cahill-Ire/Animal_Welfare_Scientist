import math
import unittest
from commons.schema import validate,ValidationError
class SchemaTests(unittest.TestCase):
    def test_numbers_exclude_booleans_and_nonfinite(self):
        for value in [True,float('nan'),float('inf')]:
            with self.assertRaises(ValidationError):validate(value,{'type':'number'})
    def test_nested_types_and_required_fields(self):
        schema={'type':'object','required':['rows'],'properties':{'rows':{'type':'array','items':{'type':'object','required':['value'],'properties':{'value':{'type':['number','null']}}}}}}
        validate({'rows':[{'value':2},{'value':None}]},schema)
        for data in [{'rows':[{}]},{'rows':[{'value':'2'}]},{'rows':[1]}]:
            with self.assertRaises(ValidationError):validate(data,schema)
