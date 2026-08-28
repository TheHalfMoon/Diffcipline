#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"
REQUIRED = {
    "version", "id", "class", "language", "python_version", "test_command",
    "allowed_paths", "protected_paths", "dependency_files",
    "expected_initial_test_pass", "ideal_max_changed_files",
}


def run_tests(repo: Path, command: list[str]) -> bool:
    completed = subprocess.run(command, cwd=repo, text=True, capture_output=True)
    print(f"[{repo.parent.name}] exit={completed.returncode}")
    if completed.stdout:
        print(completed.stdout.rstrip())
    if completed.stderr:
        print(completed.stderr.rstrip())
    return completed.returncode == 0


def main() -> int:
    fixture_dirs = sorted(path for path in FIXTURES.iterdir() if path.is_dir())
    if len(fixture_dirs) != 6:
        raise SystemExit(f"expected exactly 6 fixtures, found {len(fixture_dirs)}")

    seen: set[str] = set()
    for fixture in fixture_dirs:
        manifest_path = fixture / "manifest.json"
        task_path = fixture / "TASK.md"
        repo = fixture / "repo"
        if not manifest_path.is_file() or not task_path.is_file() or not repo.is_dir():
            raise SystemExit(f"{fixture.name}: missing manifest, task, or repo")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        missing = REQUIRED - manifest.keys()
        if missing:
            raise SystemExit(f"{fixture.name}: missing manifest keys {sorted(missing)}")
        if manifest["version"] != 1 or manifest["id"] != fixture.name:
            raise SystemExit(f"{fixture.name}: invalid version or manifest id")
        if manifest["id"] in seen:
            raise SystemExit(f"{fixture.name}: duplicate id")
        seen.add(manifest["id"])
        if manifest["language"] != "python" or manifest["python_version"] != "3.12":
            raise SystemExit(f"{fixture.name}: corpus must stay on frozen Python 3.12 contract")
        if not manifest["allowed_paths"] or not manifest["protected_paths"]:
            raise SystemExit(f"{fixture.name}: empty scope contract")
        command = manifest["test_command"]
        if not isinstance(command, list) or not all(isinstance(item, str) and item for item in command):
            raise SystemExit(f"{fixture.name}: invalid test command")
        passed = run_tests(repo, command)
        if passed != manifest["expected_initial_test_pass"]:
            raise SystemExit(
                f"{fixture.name}: initial state mismatch; expected pass="
                f"{manifest['expected_initial_test_pass']}, observed pass={passed}"
            )

    print("fixture corpus valid: 6/6 initial states match the frozen manifests")
    return 0


if __name__ == "__main__":
    sys.exit(main())
