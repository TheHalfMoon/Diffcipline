#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import shutil
import subprocess
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--arm", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--copilot", required=True, type=Path)
    parser.add_argument("--fixtures", default="benchmarks/fixtures", type=Path)
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--skill", type=Path)
    parser.add_argument("--skill-name")
    parser.add_argument("--timeout-seconds", type=int, default=480)
    parser.add_argument("--prompt-suffix", required=True)
    args = parser.parse_args()

    root = Path.cwd().resolve()
    fixtures = (root / args.fixtures).resolve()
    results = args.results.resolve()
    results.mkdir(parents=True, exist_ok=True)
    skill = args.skill.resolve() if args.skill else None
    if bool(skill) != bool(args.skill_name):
        raise SystemExit("--skill and --skill-name must be supplied together")

    for fixture_id in FIXTURES:
        fixture = fixtures / fixture_id
        out = results / fixture_id
        work = results.parent / "work" / fixture_id
        home = results.parent / "home" / fixture_id
        shutil.rmtree(out, ignore_errors=True)
        shutil.rmtree(work, ignore_errors=True)
        shutil.rmtree(home, ignore_errors=True)
        out.mkdir(parents=True)
        home.mkdir(parents=True)

        base = run(
            ["python", str(root / "benchmarks/harness/prepare_fixture.py"), str(fixture), str(work)],
            root,
            check=True,
            capture_output=True,
        ).stdout.strip()
        if skill:
            destination = home / "skills" / args.skill_name / "SKILL.md"
            destination.parent.mkdir(parents=True)
            shutil.copy2(skill, destination)

        task = (fixture / "TASK.md").read_text(encoding="utf-8").strip()
        prompt = f"{task}\n\nBenchmark constraints: {args.prompt_suffix}"
        transcript = out / "transcript.md"
        command = [
            str(args.copilot.resolve()),
            "-p",
            prompt,
            "--model",
            args.model,
            "--no-ask-user",
            "--allow-tool=write",
            "--allow-tool=shell",
            "--deny-tool=url",
            "--deny-tool=memory",
            "--deny-tool=shell(git push)",
            "--deny-tool=shell(gh:*)",
            "--share",
            str(transcript.resolve()),
        ]
        env = os.environ.copy()
        env["COPILOT_HOME"] = str(home)
        started = datetime.now(timezone.utc).isoformat()
        clock = time.monotonic()
        timed_out = False
        try:
            completed = run(
                command,
                work,
                env=env,
                capture_output=True,
                timeout=args.timeout_seconds,
            )
            exit_code = completed.returncode
            stdout, stderr = completed.stdout, completed.stderr
        except subprocess.TimeoutExpired as error:
            timed_out = True
            exit_code = 124
            stdout = error.stdout or ""
            stderr = error.stderr or ""
        duration = round(time.monotonic() - clock, 3)
        (out / "stdout.txt").write_text(stdout, encoding="utf-8", errors="replace")
        (out / "stderr.txt").write_text(stderr, encoding="utf-8", errors="replace")

        score_path = out / "score.json"
        run(
            [
                "python",
                str(root / "benchmarks/harness/score_run.py"),
                "--fixture",
                str(fixture),
                "--work",
                str(work),
                "--base",
                base,
                "--arm",
                args.arm,
                "--model",
                args.model,
                "--agent-exit-code",
                str(exit_code),
                "--transcript",
                str(transcript),
                "--output",
                str(score_path),
            ],
            root,
            check=True,
            capture_output=True,
        )
        patch = run(["git", "diff", "--binary", base, "--"], work, check=True, capture_output=True).stdout
        status = run(["git", "status", "--porcelain=v1"], work, check=True, capture_output=True).stdout
        (out / "changes.patch").write_text(patch, encoding="utf-8")
        (out / "status.txt").write_text(status, encoding="utf-8")
        shutil.copytree(work, out / "workspace", ignore=shutil.ignore_patterns(".git"))
        metadata = {
            "schema_version": 1,
            "arm": args.arm,
            "task": fixture_id,
            "model": args.model,
            "base_commit": base,
            "started_utc": started,
            "duration_seconds": duration,
            "timeout_seconds": args.timeout_seconds,
            "timed_out": timed_out,
            "agent_exit_code": exit_code,
            "skill_sha256": sha256(skill) if skill else None,
            "copilot_sha256": sha256(args.copilot),
        }
        (out / "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    scores = [json.loads((results / fixture / "score.json").read_text(encoding="utf-8")) for fixture in FIXTURES]
    summary = {
        "schema_version": 1,
        "arm": args.arm,
        "model": args.model,
        "tasks": len(scores),
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
