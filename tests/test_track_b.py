import copy
import json
import math
import subprocess
import sys
import unittest

from commons.agents import track_b as b
from commons.schema import validate, ValidationError


class TrackBTests(unittest.TestCase):
    def example(self, agent):
        return copy.deepcopy(b.SPECS[agent]["example"])

    def test_all_semantic_benchmark_cases(self):
        cases = b.benchmark_cases()
        self.assertEqual(len(cases), 32)
        for case in cases:
            with self.subTest(case=case["id"]):
                actual = b.run(case["agent_id"], case["input"])
                self.assertTrue(case["check"](actual), actual)

    def test_examples_conform_to_schemas(self):
        for agent, spec in b.SPECS.items():
            with self.subTest(agent=agent):
                validate(spec["example"], spec["input_schema"])
                validate(b.run(agent, spec["example"])["data"], spec["output_schema"])

    def test_hypothesis_preserves_threshold_without_claiming_effect(self):
        p = self.example("B1")
        p["brief"]["minimum_effect"] = 7
        r = b.run("B1", p)
        self.assertEqual(r["data"]["hypotheses"][0]["minimum_effect"], 7)
        self.assertIsNone(r["data"]["belief_forecast"]["probability"])
        self.assertTrue(r["data"]["competing_explanations"])

    def test_protocol_requires_review_and_does_not_aggregate(self):
        r = b.run("B2", self.example("B2"))
        self.assertEqual(r["status"], "awaiting_human")
        self.assertIn("no default welfare score", r["data"]["protocol_draft"]["aggregation"])
        self.assertIn("Ethics", r["data"]["review_needs"][1])

    def test_invalid_prior_and_effect_are_not_test_ready(self):
        p = self.example("B1")
        p["brief"]["prior_probability"] = 2
        p["brief"]["minimum_effect"] = -1
        r = b.run("B1", p)["data"]
        self.assertFalse(r["hypotheses"][0]["test_ready"])
        self.assertIsNone(r["belief_forecast"]["probability"])

    def test_sample_size_changes_with_effect_and_resource_constraints(self):
        p = self.example("B3")
        p["resources"]["minimum_effect"] = 1
        r = b.run("B3", p)
        self.assertEqual(r["data"]["sampling"]["approximate_units_per_arm"], 142)
        self.assertFalse(r["data"]["sampling"]["resource_feasible"])
        p["resources"]["outcome_sd"] = -1
        self.assertIsNone(b.run("B3", p)["data"]["sampling"]["approximate_units_per_arm"])

    def test_actual_pixels_drive_annotations(self):
        p = self.example("B4")
        p["video"]["frames"][1]["pixels"] = [[0, 100], [0, 0]]
        r = b.run("B4", p)
        self.assertEqual(r["data"]["annotations"][1]["mean_brightness"], 25)
        self.assertEqual(r["data"]["annotations"][1]["mean_absolute_pixel_change"], 25)
        self.assertIsNone(r["data"]["welfare_diagnosis"])
        p["video"]["frames"][1]["pixels"] = [[0], [0, 0]]
        self.assertEqual(b.run("B4", p)["status"], "abstained")

    def test_video_duration_dimensions_and_intensity_bounds(self):
        for change in ("duration", "intensity", "dimension"):
            with self.subTest(change=change):
                p = self.example("B4")
                if change == "duration":
                    p["video"]["frames"][1]["timestamp_seconds"] = 61
                elif change == "intensity":
                    p["video"]["frames"][1]["pixels"][0][0] = 256
                else:
                    p["video"]["frames"][1]["pixels"] = [[0]]
                self.assertEqual(b.run("B4", p)["status"], "abstained")

    def test_script_reproduces_statistics_and_treats_strings_as_data(self):
        p = {"rows": [{"x": 1}, {"x": 3}, {"x": None}, {"x": "__import__('os').system('false')"}, {"x": True}], "columns": ["x"], "question": "summary"}
        r = b.run("B5", p)
        stats = r["data"]["statistics"]["x"]
        self.assertEqual(stats["n"], 2)
        self.assertEqual(stats["invalid"], 2)
        self.assertEqual(stats["missing"], 1)
        self.assertEqual(stats["missing_fraction"], .2)
        self.assertAlmostEqual(stats["sample_sd"], math.sqrt(2))
        process = subprocess.run([sys.executable, "-I", "-c", r["data"]["reproducible_script"]], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(process.stdout), r["data"]["statistics"])

    def test_causal_assumptions_do_not_create_effect_estimate(self):
        p = self.example("B5")
        p["causal_assumptions"] = {key: "user claim" for key in ["exchangeability", "positivity", "consistency", "no_interference", "temporal_order", "measurement_validity"]}
        r = b.run("B5", p)
        self.assertFalse(r["data"]["causal_assessment"]["causal_effect_estimated"])
        self.assertEqual(r["data"]["causal_assessment"]["unresolved_assumptions"], [])

    def test_measurement_and_intervention_have_different_concepts(self):
        p = {"requirements": [{"id": "m", "kind": "measurement", "quantity": "temperature"}, {"id": "i", "kind": "intervention", "quantity": "temperature"}]}
        r = b.run("B6", p)["data"]
        comps = r["concept_specification"]["components"]
        self.assertNotEqual(comps[0]["class"], comps[1]["class"])
        self.assertIn("hardware cutoff", comps[1]["class"])
        self.assertFalse(r["concept_specification"]["production_ready"])

    def test_supplier_conflicts_unknown_cost_and_future_dates(self):
        p = self.example("B7")
        p["supplier_records"][0]["specifications"]["voltage"] = 5
        p["supplier_records"][0]["checked_at"] = "2027-01-01"
        del p["supplier_records"][0]["cost"]
        c = b.run("B7", p)["data"]["candidates"][0]
        self.assertEqual(c["compatibility"], "conflict")
        self.assertEqual(c["freshness"], "future_timestamp")
        self.assertIsNone(c["cost"])
        self.assertEqual(c["source_id"], "synthetic-catalogue")

    def test_criterion_units_duplicates_and_empty_criteria(self):
        p = self.example("B8")
        p["results"][0]["unit"] = "F"
        self.assertEqual(b.run("B8", p)["data"]["criteria"][0]["status"], "indeterminate")
        p = self.example("B8")
        p["results"] *= 2
        self.assertEqual(b.run("B8", p)["data"]["criteria"][0]["status"], "indeterminate")
        self.assertEqual(b.run("B8", {"criteria": [], "results": []})["data"]["recommendation"], "revise")

    def test_belief_update_requires_explicit_assumptions(self):
        p = self.example("B8")
        p["belief"] = {"prior_probability": .2, "likelihood_ratio": 4}
        self.assertIsNone(b.run("B8", p)["data"]["belief_update"]["posterior_probability"])
        p["belief"]["assumptions"] = ["Likelihood ratio provided by an independent calibration study"]
        self.assertAlmostEqual(b.run("B8", p)["data"]["belief_update"]["posterior_probability"], .5)

    def test_unexpected_outcomes_prevent_automatic_advance(self):
        p = self.example("B8")
        p["unexpected_outcomes"] = ["Power supply overheated"]
        self.assertEqual(b.run("B8", p)["data"]["recommendation"], "revise")

    def test_row_schema_rejects_wrong_shape(self):
        p = self.example("B5")
        p["rows"] = [1]
        with self.assertRaises(ValidationError):
            validate(p, b.SPECS["B5"]["input_schema"])

    def test_baselines_compute_changed_input(self):
        p = self.example("B5")
        p["rows"] = [{"reading": 10}, {"reading": 20}]
        self.assertEqual(b.baseline("B5", p)["data"]["statistics"]["reading"]["mean"], 15)
        p = self.example("B3")
        p["resources"]["available_units"] = 22
        self.assertEqual(b.baseline("B3", p)["data"]["sampling"]["approximate_units_per_arm"], 11)


if __name__ == "__main__":
    unittest.main()
