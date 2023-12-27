import unittest
import json

from ovoenergy.models.plan import OVOPlan

class TestPlan(unittest.TestCase):

    def test_plan(self):
        json_response = """{"gas": null, "electricity": {"name": "Simpler Energy - Economy 10", "exitFee": {"amount": "0", "currencyUnit": "GBX"}, "contractStartDate": "2022-01-01", "contractEndDate": null, "contractType": "variable", "isInRenewal": true, "hasFutureContracts": false, "mpxn": "123456", "msn": "123456", "personalProjection": 4000.0, "standingCharge": {"amount": "0.4505", "currencyUnit": "GBP"}, "unitRates": [{"name": "day", "unitRate": {"amount": "0.3012", "currencyUnit": "GBP"}}, {"name": "night", "unitRate": {"amount": "0.2107", "currencyUnit": "GBP"}}]}}"""
        json_dict = json.loads(json_response)
        plan = OVOPlan(**json_dict)