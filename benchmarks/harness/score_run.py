#!/usr/bin/env python3
import argparse
import fnmatch
import json
import subprocess
from pathlib import Path


def run(command: list[str], cwd: Path, check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=check)


def matches(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def changed_paths(work: Path, base: str) -> list[str]:
    tracked = run(["git", "diff", "--name-only", base, "--"], work, check=True).stdout.splitlines()
    untracked = run(["git", "ls-files", "--others", "--exclude-standard"], work, check=True).stdout.splitlines()
    return sorted(set(path for path in tracked + untracked if path))


def count_lines(work: Path, base: str) -> tuple[int, int]:
    added = deleted = 0
    output = run(["git", "diff", "--numstat", base, "--"], work, check=True).stdout
    tracked_paths: set[str] = set()
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        a, d, path = parts[0], parts[1], parts[-1]
        tracked_paths.add(path)
        if a.isdigit():
            added += int(a)
        if d.isdigit():
            deleted += int(d)
    for rel in run(["git", "ls-files", "--others", "--exclude-standard"], work, check=True).stdout.splitlines():
        if rel in tracked_paths:
            continue
        path = work / rel
        if path.is_file():
            try:
                added += len(path.read_text(encoding="utf-8").splitlines())
            except UnicodeDecodeError:
                pass
    return added, deleted


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--work", required=True, type=Path)
    parser.add_argument("--base", required=True)
    parser.add_argument("--arm", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--agent-exit-code", required=True, type=int)
    parser.add_argument("--transcript", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    manifest = json.loads((args.fixture / "manifest.json").read_text(encoding="utf-8"))
    command = manifest["test_command"]
    tests = run(command, args.work)
    correctness = tests.returncode == 0
    changed = changed_paths(args.work, args.base)
    protected = [path for path in changed if matches(path, manifest["protected_paths"])]
    unrelated = [path for path in changed if not matches(path, manifest["allowed_paths"])]
    dependency_names = set(manifest["dependency_files"])
    dependencies = [path for path in changed if Path(path).name in dependency_names]
    diff_check = run(["git", "diff", "--check", args.base, "--"], args.work)
    added, deleted = count_lines(args.work, args.base)

    transcript = ""
    if args.transcript and args.transcript.is_file():
        transcript = args.transcript.read_text(encoding="utf-8", errors="replace")
    exact_command = " ".join(command)
    if exact_command in transcript:
        verification = "full"
    elif "unittest" in transcript or "pytest" in transcript or "test" in transcript.lower():
        verification = "some"
    else:
        verification = "none"

    integrity = not protected
    passed = correctness and integrity and diff_check.returncode == 0
    result = {
        "schema_version": 1,
        "task": manifest["id"],
        "task_class": manifest["class"],
        "arm": args.arm,
        "model": args.model,
        "base_commit": args.base,
        "agent_exit_code": args.agent_exit_code,
        "pass": passed,
        "correctness": correctness,
        "protected_file_integrity": integrity,
        "diff_check_pass": diff_check.returncode == 0,
        "changed_files": len(changed),
        "changed_paths": changed,
        "added_lines": added,
        "deleted_lines": deleted,
        "unrelated_paths": unrelated,
        "dependency_paths": dependencies,
        "verification": verification,
        "ideal_max_changed_files": manifest["ideal_max_changed_files"],
        "test_command": command,
        "test_exit_code": tests.returncode,
        "test_output": (tests.stdout + tests.stderr)[-12000:],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
