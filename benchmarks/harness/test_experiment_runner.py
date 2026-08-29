import copy
import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

HARNESS = Path(__file__).resolve().parent
ROOT = HARNESS.parents[1]
sys.path.insert(0, str(HARNESS))
MODULE = importlib.import_module("experiment_runner")
CONFIG = json.loads((ROOT / "benchmarks/v0.3/experiment.json").read_text(encoding="utf-8"))


class ExperimentRunnerTests(unittest.TestCase):
    def test_matrix_is_deterministic_and_matched(self) -> None:
        first = MODULE.expand_matrix(CONFIG)
        reordered = copy.deepcopy(CONFIG)
        reordered["executors"].reverse()
        reordered["treatments"].reverse()
        second = MODULE.expand_matrix(reordered)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 24)
        MODULE.assert_matched(first)
        by_fixture = {}
        for row in first:
            by_fixture.setdefault((row["executor_id"], row["fixture_id"]), set()).add(
                row["contract_sha256"]
            )
        self.assertTrue(all(len(values) == 1 for values in by_fixture.values()))

    def test_matching_rejects_contract_tamper_and_duplicate_rows(self) -> None:
        rows = MODULE.expand_matrix(CONFIG)
        tampered = copy.deepcopy(rows)
        tampered[1]["contract_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            MODULE.assert_matched(tampered)
        duplicate = copy.deepcopy(rows)
        duplicate.append(copy.deepcopy(rows[0]))
        with self.assertRaises(ValueError):
            MODULE.assert_matched(duplicate)

    def test_attempt_reservation_never_overwrites(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            first_id, first = MODULE.reserve_attempt(root)
            (first / "marker").write_text("preserve", encoding="utf-8")
            second_id, second = MODULE.reserve_attempt(root)
            self.assertEqual((first_id, second_id), ("attempt-001", "attempt-002"))
            self.assertEqual((first / "marker").read_text(encoding="utf-8"), "preserve")
            self.assertNotEqual(first, second)

    def test_manifest_requires_every_row_and_preserves_all_statuses(self) -> None:
        rows = MODULE.expand_matrix(CONFIG)[:4]
        statuses = ["included", "failed", "timed_out", "excluded"]
        records = {}
        for row, status in zip(rows, statuses, strict=True):
            key = (row["executor_id"], row["treatment_id"], row["fixture_id"])
            records[key] = {
                "status": status,
                "reason": None if status == "included" else f"{status} reason",
            }
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "manifest.json"
            manifest = MODULE.write_manifest("attempt-007", rows, records, path)
            self.assertEqual(
                manifest["counts"], {status: 1 for status in sorted(MODULE.STATUSES)}
            )
            self.assertEqual(
                {run["status"] for run in manifest["runs"]},
                MODULE.STATUSES,
            )
            missing = dict(records)
            missing.pop(next(iter(missing)))
            with self.assertRaises(ValueError):
                MODULE.write_manifest("attempt-008", rows, missing, path)

    def test_arm_command_preserves_executor_contract(self) -> None:
        config = MODULE.normalize_config(CONFIG)
        executor = config["executors"][0]
        baseline = next(item for item in config["treatments"] if item["id"] == "baseline")
        command = MODULE.build_arm_command(
            ROOT,
            config,
            executor,
            baseline,
            Path("/tmp/results"),
            None,
            "http://127.0.0.1:8080",
        )
        self.assertIn(executor["adapter_kind"], command)
        self.assertIn(executor["model"]["id"], command)
        self.assertIn(str(executor["resource_limits"]["per_task_timeout_seconds"]), command)
        self.assertNotIn("--skill", command)

    def test_blob_digest_and_map_parsing_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "skill.md"
            path.write_text("proof\n", encoding="utf-8")
            data = path.read_bytes()
            expected = __import__("hashlib").sha1(
                f"blob {len(data)}\0".encode() + data
            ).hexdigest()
            self.assertEqual(MODULE.git_blob_sha1(path), expected)
        self.assertEqual(
            MODULE.parse_map(["one=http://local"], "endpoint"), {"one": "http://local"}
        )
        with self.assertRaises(ValueError):
            MODULE.parse_map(["one=a", "one=b"], "endpoint")


if __name__ == "__main__":
    unittest.main()
