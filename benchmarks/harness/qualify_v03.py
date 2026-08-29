#!/usr/bin/env python3
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from experiment_config import normalize_config
from experiment_runner import assert_matched, expand_matrix, write_manifest

FIXTURE_REVISION = "cde4d0058ce522ddd9863457c29560679fac53dd"
FROZEN_BLOBS = {
    "benchmarks/run-config.json": "502452d80e1cacd6e1e8becfad38de46ffa71465",
    "benchmarks/harness/prepare_fixture.py": "59224e52e6ecff95114b77df4c6c173cc038e3c6",
    "benchmarks/harness/score_run.py": "251967ddad495c090cdb2b8c7d7c9e467e0d5dd3",
}


def run(command: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=check)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_frozen_boundary(root: Path) -> None:
    run(
        [
            "git",
            "diff",
            "--exit-code",
            FIXTURE_REVISION,
            "--",
            "benchmarks/fixtures",
            "benchmarks/harness/prepare_fixture.py",
            "benchmarks/harness/score_run.py",
        ],
        root,
    )
    for relative, expected in FROZEN_BLOBS.items():
        actual = run(["git", "hash-object", relative], root).stdout.strip()
        if actual != expected:
            raise ValueError(f"frozen benchmark blob changed: {relative}")


def qualify_contract_adapter(root: Path) -> None:
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        work = base / "work"
        work.mkdir()
        transcript = base / "transcript.md"
        prompt = json.dumps({"action": "write", "path": "qualified.txt", "content": "qualified\n"})
        completed = run(
            [
                sys.executable,
                str(root / "benchmarks/harness/executor_adapter.py"),
                "--adapter-kind",
                "contract-test",
                "--workdir",
                str(work),
                "--prompt",
                prompt,
                "--transcript",
                str(transcript),
                "--timeout-seconds",
                "5",
            ],
            root,
            check=False,
        )
        if completed.returncode != 0:
            raise ValueError(f"contract adapter failed: {completed.stderr}")
        if (work / "qualified.txt").read_text(encoding="utf-8") != "qualified\n":
            raise ValueError("contract adapter did not preserve deterministic output")
        if not transcript.is_file():
            raise ValueError("contract adapter did not preserve transcript evidence")


def qualify_matrix(root: Path) -> tuple[dict, int]:
    config_path = root / "benchmarks/v0.3/experiment.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    normalized = normalize_config(config)
    rows = expand_matrix(normalized)
    assert_matched(rows)
    expected = len(normalized["executors"]) * len(normalized["treatments"]) * 6
    if len(rows) != expected:
        raise ValueError(f"matrix size mismatch: {len(rows)} != {expected}")
    with tempfile.TemporaryDirectory() as temp:
        manifest_path = Path(temp) / "manifest.json"
        records = {
            (row["executor_id"], row["treatment_id"], row["fixture_id"]): {
                "status": "included",
                "reason": None,
            }
            for row in rows
        }
        manifest = write_manifest("qualification", rows, records, manifest_path)
        if manifest["counts"]["included"] != expected or len(manifest["runs"]) != expected:
            raise ValueError("qualification manifest is incomplete")
    return normalized, len(rows)


def qualify_scorer(root: Path) -> None:
    fixture = root / "benchmarks/fixtures/f06-already-minimal"
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        work = base / "work"
        score = base / "score.json"
        prepared = run(
            [sys.executable, str(root / "benchmarks/harness/prepare_fixture.py"), str(fixture), str(work)],
            root,
        ).stdout.strip()
        run(
            [
                sys.executable,
                str(root / "benchmarks/harness/score_run.py"),
                "--fixture",
                str(fixture),
                "--work",
                str(work),
                "--base",
                prepared,
                "--arm",
                "qualification",
                "--model",
                "contract-test",
                "--agent-exit-code",
                "0",
                "--output",
                str(score),
            ],
            root,
        )
        result = json.loads(score.read_text(encoding="utf-8"))
        if not result["pass"] or not result["correctness"] or result["changed_files"] != 0:
            raise ValueError("objective scorer qualification failed")


def qualify(root: Path) -> dict:
    verify_frozen_boundary(root)
    run([sys.executable, "benchmarks/harness/validate_fixtures.py"], root)
    qualify_contract_adapter(root)
    normalized, matrix_rows = qualify_matrix(root)
    qualify_scorer(root)
    revision = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
    return {
        "schema_version": 1,
        "benchmark_version": "v0.3",
        "repository_revision": revision,
        "fixture_revision": FIXTURE_REVISION,
        "matrix_rows": matrix_rows,
        "executor_ids": [item["id"] for item in normalized["executors"]],
        "treatment_ids": [item["id"] for item in normalized["treatments"]],
        "sandbox_contracts": {item["id"]: item["sandbox"] for item in normalized["executors"]},
        "resource_limits": {item["id"]: item["resource_limits"] for item in normalized["executors"]},
        "private_credentials_required": False,
        "comparative_model_execution": False,
        "frozen_v0_1_blobs": FROZEN_BLOBS,
        "config_sha256": sha256(root / "benchmarks/v0.3/experiment.json"),
        "adapter_sha256": sha256(root / "benchmarks/harness/executor_adapter.py"),
        "agent_sha256": sha256(root / "benchmarks/harness/local_agent.py"),
        "sandbox_sha256": sha256(root / "benchmarks/harness/sandbox_exec.py"),
        "run_arm_sha256": sha256(root / "benchmarks/harness/run_arm.py"),
        "runner_sha256": sha256(root / "benchmarks/harness/experiment_runner.py"),
        "result": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    root = Path.cwd().resolve()
    evidence = qualify(root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
