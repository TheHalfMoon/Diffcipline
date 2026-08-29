#!/usr/bin/env python3
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

FIXTURES = [
    "f01-shared-root-cause",
    "f02-stdlib-query",
    "f03-dependency-temptation",
    "f04-refactor-preserve",
    "f05-security-boundary",
    "f06-already-minimal",
]


def run(command: list[str], cwd: Path, **kwargs) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, **kwargs)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def timeout_text(value: str | bytes | None) -> str:
    return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value or ""


def capture_process(
    command: list[str], cwd: Path, timeout_seconds: float, grace_seconds: float = 5
) -> tuple[int, str, str, bool]:
    try:
        completed = run(command, cwd, capture_output=True, timeout=timeout_seconds + grace_seconds)
        return completed.returncode, completed.stdout, completed.stderr, False
    except subprocess.TimeoutExpired as error:
        return 124, timeout_text(error.stdout), timeout_text(error.stderr), True


def validate_adapter_for_arm(adapter_kind: str) -> None:
    if adapter_kind == "contract-test":
        raise ValueError("contract-test adapter is qualification-only and cannot produce comparative arm evidence")


def build_adapter_command(
    root: Path,
    adapter_kind: str,
    workdir: Path,
    prompt: str,
    transcript: Path,
    timeout_seconds: int,
    model: str | None,
    base_url: str | None,
    treatment: Path | None,
) -> list[str]:
    command = [
        sys.executable,
        str(root / "benchmarks/harness/executor_adapter.py"),
        "--adapter-kind", adapter_kind,
        "--workdir", str(workdir),
        "--prompt", prompt,
        "--transcript", str(transcript),
        "--timeout-seconds", str(timeout_seconds),
    ]
    if model:
        command += ["--model", model]
    if base_url:
        command += ["--base-url", base_url]
    if treatment:
        command += ["--treatment", str(treatment)]
    return command


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--arm", required=True)
    parser.add_argument("--adapter-kind", default="local-openai-tool-loop")
    parser.add_argument("--model")
    parser.add_argument("--base-url")
    parser.add_argument("--fixtures", default="benchmarks/fixtures", type=Path)
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--skill", type=Path)
    parser.add_argument("--skill-name")
    parser.add_argument("--timeout-seconds", type=int, default=480)
    parser.add_argument("--prompt-suffix", required=True)
    args = parser.parse_args()

    try:
        validate_adapter_for_arm(args.adapter_kind)
    except ValueError as error:
        raise SystemExit(str(error))
    root = Path.cwd().resolve()
    fixtures = (root / args.fixtures).resolve()
    results = args.results.resolve()
    results.mkdir(parents=True, exist_ok=True)
    skill = args.skill.resolve() if args.skill else None
    adapter = root / "benchmarks/harness/executor_adapter.py"
    if bool(skill) != bool(args.skill_name):
        raise SystemExit("--skill and --skill-name must be supplied together")

    for fixture_id in FIXTURES:
        fixture = fixtures / fixture_id
        out = results / fixture_id
        work = results.parent / "work" / fixture_id
        shutil.rmtree(out, ignore_errors=True)
        shutil.rmtree(work, ignore_errors=True)
        out.mkdir(parents=True)
        base = run(
            ["python", str(root / "benchmarks/harness/prepare_fixture.py"), str(fixture), str(work)],
            root, check=True, capture_output=True,
        ).stdout.strip()

        task = (fixture / "TASK.md").read_text(encoding="utf-8").strip()
        prompt = f"{task}\n\nBenchmark constraints: {args.prompt_suffix}"
        transcript = out / "transcript.md"
        command = build_adapter_command(
            root, args.adapter_kind, work, prompt, transcript, args.timeout_seconds,
            args.model, args.base_url, skill,
        )
        started = datetime.now(timezone.utc).isoformat()
        clock = time.monotonic()
        exit_code, stdout, stderr, timed_out = capture_process(
            command, root, args.timeout_seconds
        )
        duration = round(time.monotonic() - clock, 3)
        (out / "stdout.txt").write_text(stdout, encoding="utf-8", errors="replace")
        (out / "stderr.txt").write_text(stderr, encoding="utf-8", errors="replace")

        score_path = out / "score.json"
        run(
            [
                "python", str(root / "benchmarks/harness/score_run.py"),
                "--fixture", str(fixture), "--work", str(work), "--base", base,
                "--arm", args.arm, "--model", args.model or args.adapter_kind,
                "--agent-exit-code", str(exit_code),
                "--transcript", str(transcript), "--output", str(score_path),
            ],
            root, check=True, capture_output=True,
        )
        patch = run(["git", "diff", "--binary", base, "--"], work, check=True, capture_output=True).stdout
        status = run(["git", "status", "--porcelain=v1"], work, check=True, capture_output=True).stdout
        (out / "changes.patch").write_text(patch, encoding="utf-8")
        (out / "status.txt").write_text(status, encoding="utf-8")
        shutil.copytree(work, out / "workspace", ignore=shutil.ignore_patterns(".git"))
        treatment_sha = sha256(skill) if skill else None
        metadata = {
            "schema_version": 1, "arm": args.arm, "task": fixture_id,
            "adapter_kind": args.adapter_kind, "model": args.model,
            "base_commit": base, "started_utc": started, "duration_seconds": duration,
            "timeout_seconds": args.timeout_seconds, "timed_out": timed_out,
            "agent_exit_code": exit_code, "skill_sha256": treatment_sha,
            "treatment_sha256": treatment_sha, "adapter_harness_sha256": sha256(adapter),
        }
        if args.adapter_kind == "local-openai-tool-loop":
            metadata["agent_harness_sha256"] = sha256(root / "benchmarks/harness/local_agent.py")
        (out / "metadata.json").write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

    scores = [json.loads((results / fixture / "score.json").read_text(encoding="utf-8")) for fixture in FIXTURES]
    summary = {
        "schema_version": 1, "arm": args.arm, "model": args.model, "tasks": len(scores),
        "passed": sum(1 for score in scores if score["pass"]),
        "correct": sum(1 for score in scores if score["correctness"]),
        "changed_files": sum(score["changed_files"] for score in scores),
        "added_lines": sum(score["added_lines"] for score in scores),
        "deleted_lines": sum(score["deleted_lines"] for score in scores),
        "dependency_changes": sum(len(score["dependency_paths"]) for score in scores),
        "unrelated_changes": sum(len(score["unrelated_paths"]) for score in scores),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
