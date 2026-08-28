#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
from pathlib import Path


def run(*args: str, cwd: Path) -> str:
    completed = subprocess.run(args, cwd=cwd, check=True, text=True, capture_output=True)
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
    run("git", "commit", "-q", "-m", f"benchmark baseline: {manifest['id']}", cwd=output)
    print(run("git", "rev-parse", "HEAD", cwd=output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
