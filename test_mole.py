import unittest
from mole import MoleEvaluator, MoleConfig

class TestMole(unittest.TestCase):
    def test_healthy_case_low_gap(self):
        ev = MoleEvaluator()
        out = ev.evaluate(0.95, {"a":0.1,"b":0.1})
        self.assertLess(out["observability_gap"],0.2)

    def test_masked_failure_detected(self):
        ev = MoleEvaluator(config=MoleConfig(gap_threshold=0.2,min_coverage=0.5))
        out = ev.evaluate(0.95, {"a":0.8,"b":0.7,"c":0.6})
        self.assertTrue(out["hidden_failure"])

    def test_visible_failure_reduces_gap(self):
        ev = MoleEvaluator()
        deep = {"a":0.8,"b":0.8}
        hidden = ev.evaluate(0.95,deep)
        visible = ev.evaluate(0.4,deep)
        self.assertGreater(hidden["observability_gap"], visible["observability_gap"])

if __name__ == "__main__":
    unittest.main()
