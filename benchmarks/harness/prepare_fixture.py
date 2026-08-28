#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path


FIXTURE_COMMIT_DATE = "2000-01-01T00:00:00Z"


def run(*args: str, cwd: Path, env: dict[str, str] | None = None) -> str:
    completed = subprocess.run(
        args, cwd=cwd, check=True, text=True, capture_output=True, env=env
    )
    return completed.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    fixture = args.fixture.resolve()
    output = args.output.resolve()
    manifest = json.loads((fixture / "manifest.json").read_text(encoding="utf-8"))
    repo = fixture / "repo"
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(repo, output)

    run("git", "init", "-q", cwd=output)
    run("git", "config", "user.name", "Diffcipline Benchmark", cwd=output)
    run("git", "config", "user.email", "benchmark@diffcipline.invalid", cwd=output)
    run("git", "add", ".", cwd=output)
    commit_env = os.environ.copy()
    commit_env.update(
        GIT_AUTHOR_DATE=FIXTURE_COMMIT_DATE,
        GIT_COMMITTER_DATE=FIXTURE_COMMIT_DATE,
    )
    run(
        "git",
        "commit",
        "-q",
        "-m",
        f"benchmark baseline: {manifest['id']}",
        cwd=output,
        env=commit_env,
    )
    print(run("git", "rev-parse", "HEAD", cwd=output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
