import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = Path(__file__).with_name("experiment_config.py")
SPEC = importlib.util.spec_from_file_location("experiment_config", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
CONFIG_PATH = ROOT / "benchmarks" / "v0.3" / "experiment.json"


class ExperimentConfigTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

    def invalid(self, mutate) -> None:
        candidate = copy.deepcopy(self.config)
        mutate(candidate)
        with self.assertRaises(ValueError):
            MODULE.validate_config(candidate)

    def test_canonical_config_is_valid_and_deterministic(self) -> None:
        MODULE.validate_config(self.config)
        first = MODULE.serialize_normalized(self.config)
        reordered = copy.deepcopy(self.config)
        reordered["executors"].reverse()
        reordered["treatments"].reverse()
        self.assertEqual(first, MODULE.serialize_normalized(reordered))
        self.assertEqual(first, MODULE.serialize_normalized(json.loads(first)))

    def test_duplicate_and_malformed_ids_fail_closed(self) -> None:
        self.invalid(lambda c: c["treatments"].append(copy.deepcopy(c["treatments"][0])))
        self.invalid(lambda c: c["executors"][0].update(id="Bad ID"))

    def test_unsupported_adapter_and_treatment_fail_closed(self) -> None:
        self.invalid(lambda c: c["executors"][0].update(adapter_kind="unknown"))
        self.invalid(lambda c: c["treatments"][1].update(kind="prompt"))

    def test_revision_and_digest_validation_fail_closed(self) -> None:
        self.invalid(lambda c: c["executors"][0]["runtime"].update(revision="main"))
        self.invalid(lambda c: c["treatments"][1]["source"]["digest"].update(value="0" * 39))

    def test_unsafe_permissions_and_bad_limits_fail_closed(self) -> None:
        self.invalid(lambda c: c["executors"][0]["permissions"].update(network_tools="allowed"))
        self.invalid(lambda c: c["executors"][0]["resource_limits"].update(per_task_timeout_seconds=0))

    def test_baseline_and_diffcipline_are_required(self) -> None:
        self.invalid(lambda c: c.update(treatments=[t for t in c["treatments"] if t["id"] != "baseline"]))
        self.invalid(lambda c: c.update(treatments=[t for t in c["treatments"] if t["id"] != "diffcipline"]))


if __name__ == "__main__":
    unittest.main()
