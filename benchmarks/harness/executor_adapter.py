#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ADAPTER_KINDS = {"local-openai-tool-loop", "contract-test"}


def record(path: Path, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"## {title}\n\n{body.rstrip()}\n\n")


def local_command(root: Path, args: argparse.Namespace) -> list[str]:
    if not args.base_url or not args.model:
        raise ValueError("local-openai-tool-loop requires --base-url and --model")
    command = [
        sys.executable,
        str(root / "benchmarks/harness/local_agent.py"),
        "--base-url", args.base_url,
        "--model", args.model,
        "--workdir", str(args.workdir),
        "--prompt", args.prompt,
        "--transcript", str(args.transcript),
        "--timeout-seconds", str(args.timeout_seconds),
    ]
    sandbox_image = getattr(args, "sandbox_image", None)
    sandbox_cpu = getattr(args, "sandbox_cpu_cores", None)
    sandbox_memory = getattr(args, "sandbox_memory_gb", None)
    sandbox_values = (sandbox_image, sandbox_cpu, sandbox_memory)
    if any(value is not None for value in sandbox_values):
        if not all(value is not None for value in sandbox_values):
            raise ValueError("sandbox image, cpu cores, and memory must be supplied together")
        command += [
            "--sandbox-image", sandbox_image,
            "--sandbox-cpu-cores", str(sandbox_cpu),
            "--sandbox-memory-gb", str(sandbox_memory),
        ]
    if args.treatment:
        command += ["--skill", str(args.treatment)]
    return command


def safe_target(workdir: Path, raw: object) -> Path:
    if not isinstance(raw, str) or not raw:
        raise ValueError("contract-test write path must be non-empty")
    relative = Path(raw)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("contract-test write path must stay inside workdir")
    target = (workdir / relative).resolve()
    try:
        target.relative_to(workdir.resolve())
    except ValueError as error:
        raise ValueError("contract-test write path escapes workdir") from error
    return target


def run_contract_test(args: argparse.Namespace) -> int:
    try:
        instruction = json.loads(args.prompt)
    except json.JSONDecodeError as error:
        raise ValueError("contract-test prompt must be a JSON object") from error
    if not isinstance(instruction, dict):
        raise ValueError("contract-test prompt must be a JSON object")
    args.transcript.parent.mkdir(parents=True, exist_ok=True)
    args.transcript.write_text("# Contract-test executor transcript\n\n", encoding="utf-8")
    record(args.transcript, "Prompt", args.prompt)
    if args.treatment:
        record(args.transcript, "Treatment: skill", args.treatment.read_text(encoding="utf-8"))

    action = instruction.get("action")
    if action == "write":
        target = safe_target(args.workdir, instruction.get("path"))
        content = instruction.get("content")
        if not isinstance(content, str):
            raise ValueError("contract-test write content must be a string")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        record(args.transcript, "Contract action", f"wrote {target.relative_to(args.workdir.resolve())}")
        print(f"contract-test wrote {target.relative_to(args.workdir.resolve())}")
        return 0
    if action == "exit":
        code = instruction.get("code")
        if not isinstance(code, int) or isinstance(code, bool) or not 0 <= code <= 125:
            raise ValueError("contract-test exit code must be an integer from 0 through 125")
        stdout = instruction.get("stdout", "")
        stderr = instruction.get("stderr", "")
        if not isinstance(stdout, str) or not isinstance(stderr, str):
            raise ValueError("contract-test stdout and stderr must be strings")
        if stdout:
            print(stdout, end="")
        if stderr:
            print(stderr, end="", file=sys.stderr)
        record(args.transcript, "Contract action", f"exit {code}")
        return code
    raise ValueError("contract-test action must be write or exit")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--adapter-kind", required=True, choices=sorted(ADAPTER_KINDS))
    parser.add_argument("--workdir", required=True, type=Path)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--transcript", required=True, type=Path)
    parser.add_argument("--timeout-seconds", required=True, type=int)
    parser.add_argument("--treatment", type=Path)
    parser.add_argument("--base-url")
    parser.add_argument("--model")
    parser.add_argument("--sandbox-image")
    parser.add_argument("--sandbox-cpu-cores", type=int)
    parser.add_argument("--sandbox-memory-gb", type=int)
    args = parser.parse_args()
    args.workdir = args.workdir.resolve()
    args.transcript = args.transcript.resolve()
    args.treatment = args.treatment.resolve() if args.treatment else None
    try:
        if args.adapter_kind == "contract-test":
            return run_contract_test(args)
        root = Path.cwd().resolve()
        return subprocess.run(local_command(root, args), cwd=root).returncode
    except Exception as error:
        record(args.transcript, "Adapter error", repr(error))
        print(f"adapter error: {error}", file=os.sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
