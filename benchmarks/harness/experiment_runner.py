#!/usr/bin/env python3
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

from experiment_config import normalize_config

FIXTURES = (
    "f01-shared-root-cause",
    "f02-stdlib-query",
    "f03-dependency-temptation",
    "f04-refactor-preserve",
    "f05-security-boundary",
    "f06-already-minimal",
)
STATUSES = {"included", "failed", "timed_out", "excluded"}


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def treatment_sort_key(treatment: dict) -> tuple[int, str]:
    treatment_id = treatment["id"]
    if treatment_id == "baseline":
        return (0, treatment_id)
    if treatment_id == "diffcipline":
        return (2, treatment_id)
    return (1, treatment_id)


def ordered_treatments(config: dict) -> list[dict]:
    return sorted(config["treatments"], key=treatment_sort_key)


def contract_for(config: dict, executor: dict, fixture_id: str) -> dict:
    return {
        "benchmark_version": config["benchmark_version"],
        "fixture_revision": config["fixture_revision"],
        "prompt_suffix": config["prompt_suffix"],
        "fixture_id": fixture_id,
        "executor": executor,
    }


def contract_digest(contract: dict) -> str:
    return hashlib.sha256(canonical_json(contract).encode()).hexdigest()


def expand_matrix(config: object, fixtures: tuple[str, ...] = FIXTURES) -> list[dict]:
    normalized = normalize_config(config)
    rows: list[dict] = []
    for executor in normalized["executors"]:
        for treatment in ordered_treatments(normalized):
            for fixture_id in sorted(fixtures):
                contract = contract_for(normalized, executor, fixture_id)
                rows.append(
                    {
                        "executor_id": executor["id"],
                        "treatment_id": treatment["id"],
                        "fixture_id": fixture_id,
                        "contract_sha256": contract_digest(contract),
                    }
                )
    return rows


def assert_matched(rows: list[dict]) -> None:
    groups: dict[tuple[str, str], set[str]] = {}
    treatments: dict[tuple[str, str], set[str]] = {}
    for row in rows:
        key = (row["executor_id"], row["fixture_id"])
        groups.setdefault(key, set()).add(row["contract_sha256"])
        ids = treatments.setdefault(key, set())
        if row["treatment_id"] in ids:
            raise ValueError(f"duplicate matrix row: {key} {row['treatment_id']}")
        ids.add(row["treatment_id"])
    mismatched = [key for key, digests in groups.items() if len(digests) != 1]
    if mismatched:
        raise ValueError(f"unmatched comparison contracts: {mismatched}")


def reserve_attempt(output: Path) -> tuple[str, Path]:
    output.mkdir(parents=True, exist_ok=True)
    attempts = []
    for path in output.iterdir():
        if path.is_dir() and path.name.startswith("attempt-") and path.name[8:].isdigit():
            attempts.append(int(path.name[8:]))
    number = max(attempts, default=0) + 1
    attempt_id = f"attempt-{number:03d}"
    path = output / attempt_id
    path.mkdir(exist_ok=False)
    return attempt_id, path


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def treatment_path(treatment: dict, root: Path) -> Path | None:
    if treatment["kind"] == "none":
        return None
    path = root / treatment["id"] / "SKILL.md"
    if not path.is_file():
        raise ValueError(f"{treatment['id']}: missing treatment file: {path}")
    expected = treatment["source"]["digest"]["value"]
    actual = git_blob_sha1(path)
    if actual != expected:
        raise ValueError(f"{treatment['id']}: treatment digest mismatch")
    return path


def build_arm_command(
    root: Path,
    config: dict,
    executor: dict,
    treatment: dict,
    results: Path,
    treatment_file: Path | None,
    base_url: str,
) -> list[str]:
    command = [
        sys.executable,
        str(root / "benchmarks/harness/run_arm.py"),
        "--arm",
        treatment["id"],
        "--adapter-kind",
        executor["adapter_kind"],
        "--model",
        executor["model"]["id"],
        "--base-url",
        base_url,
        "--results",
        str(results),
        "--timeout-seconds",
        str(executor["resource_limits"]["per_task_timeout_seconds"]),
        "--prompt-suffix",
        config["prompt_suffix"],
        "--sandbox-image",
        executor["sandbox"]["image"],
        "--sandbox-cpu-cores",
        str(executor["resource_limits"]["cpu_cores"]),
        "--sandbox-memory-gb",
        str(executor["resource_limits"]["memory_gb"]),
    ]
    if treatment_file:
        command += ["--skill", str(treatment_file), "--skill-name", treatment["id"]]
    return command


def enrich_bundle(bundle: Path, attempt_id: str, row: dict) -> dict:
    metadata_path = bundle / "metadata.json"
    score_path = bundle / "score.json"
    if not metadata_path.is_file() or not score_path.is_file():
        return {"status": "failed", "reason": "missing run metadata or scorer output"}
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata.update(
        experiment_attempt=attempt_id,
        executor_id=row["executor_id"],
        treatment_id=row["treatment_id"],
        comparison_contract_sha256=row["contract_sha256"],
    )
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if metadata.get("timed_out"):
        return {"status": "timed_out", "reason": "executor timed out"}
    if metadata.get("agent_exit_code") != 0:
        return {"status": "failed", "reason": f"executor exit {metadata.get('agent_exit_code')}"}
    return {"status": "included", "reason": None}


def write_manifest(
    attempt_id: str,
    rows: list[dict],
    records: dict[tuple[str, str, str], dict],
    path: Path,
) -> dict:
    entries = []
    counts = {status: 0 for status in sorted(STATUSES)}
    for row in rows:
        key = (row["executor_id"], row["treatment_id"], row["fixture_id"])
        if key not in records:
            raise ValueError(f"missing manifest record: {key}")
        record = records[key]
        status = record.get("status")
        if status not in STATUSES:
            raise ValueError(f"invalid manifest status: {status}")
        reason = record.get("reason")
        if status != "included" and not isinstance(reason, str):
            raise ValueError(f"{key}: non-included run requires a reason")
        counts[status] += 1
        entries.append({**row, "attempt": attempt_id, "status": status, "reason": reason})
    manifest = {"schema_version": 1, "attempt": attempt_id, "counts": counts, "runs": entries}
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def parse_map(values: list[str], label: str) -> dict[str, str]:
    result = {}
    for value in values:
        key, separator, item = value.partition("=")
        if not separator or not key or not item or key in result:
            raise ValueError(f"invalid {label}: {value}")
        result[key] = item
    return result


def execute(
    config: dict,
    output: Path,
    treatments_root: Path,
    endpoints: dict[str, str],
) -> Path:
    normalized = normalize_config(config)
    rows = expand_matrix(normalized)
    assert_matched(rows)
    executors = {item["id"]: item for item in normalized["executors"]}
    treatments = {item["id"]: item for item in normalized["treatments"]}
    ordered = ordered_treatments(normalized)
    for executor_id in executors:
        if executor_id not in endpoints:
            raise ValueError(f"{executor_id}: missing endpoint")
    treatment_files = {
        key: treatment_path(value, treatments_root) for key, value in treatments.items()
    }
    attempt_id, attempt = reserve_attempt(output)
    records = {}
    root = Path.cwd().resolve()
    for executor_id, executor in executors.items():
        for treatment in ordered:
            treatment_id = treatment["id"]
            results = attempt / executor_id / treatment_id
            command = build_arm_command(
                root,
                normalized,
                executor,
                treatment,
                results,
                treatment_files[treatment_id],
                endpoints[executor_id],
            )
            completed = subprocess.run(command, cwd=root)
            for row in rows:
                if row["executor_id"] != executor_id or row["treatment_id"] != treatment_id:
                    continue
                key = (executor_id, treatment_id, row["fixture_id"])
                record = enrich_bundle(results / row["fixture_id"], attempt_id, row)
                if completed.returncode != 0 and record["status"] == "included":
                    record = {
                        "status": "failed",
                        "reason": f"arm process exit {completed.returncode}",
                    }
                records[key] = record
    write_manifest(attempt_id, rows, records, attempt / "manifest.json")
    return attempt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path("benchmarks/v0.3/experiment.json"))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--treatments-root", required=True, type=Path)
    parser.add_argument("--endpoint", action="append", default=[])
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    rows = expand_matrix(config)
    assert_matched(rows)
    if args.plan:
        print(json.dumps(rows, indent=2, sort_keys=True))
        return 0
    endpoints = parse_map(args.endpoint, "endpoint")
    attempt = execute(config, args.output, args.treatments_root, endpoints)
    print(attempt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
