#!/usr/bin/env python3
import argparse
import os
import re
import subprocess
import uuid
from pathlib import Path

IMAGE_RE = re.compile(r"^[a-z0-9][a-z0-9._/-]*:[A-Za-z0-9._-]+@sha256:[0-9a-f]{64}$")
ENV_ALLOW = ("LANG", "LC_ALL", "LC_CTYPE")
FIXED_PATH = "/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin"


def validate_image(image: str) -> None:
    if not IMAGE_RE.fullmatch(image):
        raise ValueError("sandbox image must be pinned as name:tag@sha256:<64-hex>")


def positive(value: int, label: str) -> None:
    if isinstance(value, bool) or value <= 0:
        raise ValueError(f"{label} must be a positive integer")


def sandbox_environment(source: dict[str, str] | None = None) -> dict[str, str]:
    source = os.environ if source is None else source
    env = {key: source[key] for key in ENV_ALLOW if source.get(key)}
    env.update(
        PATH=FIXED_PATH,
        HOME="/tmp",
        TMPDIR="/tmp",
        PYTHONDONTWRITEBYTECODE="1",
        GIT_CONFIG_NOSYSTEM="1",
        GIT_CONFIG_GLOBAL="/tmp/gitconfig",
    )
    return env


def docker_command(
    image: str,
    workdir: Path,
    command: str,
    container_name: str,
    cpu_cores: int,
    memory_gb: int,
    source_env: dict[str, str] | None = None,
) -> list[str]:
    validate_image(image)
    positive(cpu_cores, "sandbox cpu_cores")
    positive(memory_gb, "sandbox memory_gb")
    workdir = workdir.resolve()
    if not workdir.is_dir():
        raise ValueError("sandbox workdir must be an existing directory")
    result = [
        "docker", "run", "--rm", "--pull=never", "--name", container_name,
        "--network", "none",
        "--read-only",
        "--cap-drop", "ALL",
        "--security-opt", "no-new-privileges:true",
        "--pids-limit", "256",
        "--cpus", str(cpu_cores),
        "--memory", f"{memory_gb}g",
        "--memory-swap", f"{memory_gb}g",
        "--user", f"{os.getuid()}:{os.getgid()}",
        "--workdir", "/workspace",
        "--mount", f"type=bind,src={workdir},dst=/workspace",
        "--tmpfs", "/tmp:rw,nosuid,nodev,noexec,size=64m",
    ]
    for key, value in sandbox_environment(source_env).items():
        result += ["--env", f"{key}={value}"]
    result += [image, "/bin/bash", "--noprofile", "--norc", "-lc", command]
    return result


def run_sandboxed(
    image: str,
    workdir: Path,
    command: str,
    timeout_seconds: float,
    cpu_cores: int,
    memory_gb: int,
    source_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    name = f"diffcipline-tool-{os.getpid()}-{uuid.uuid4().hex[:12]}"
    argv = docker_command(
        image, workdir, command, name, cpu_cores, memory_gb, source_env
    )
    try:
        return subprocess.run(
            argv,
            text=True,
            capture_output=True,
            timeout=max(1, timeout_seconds),
            check=False,
        )
    except subprocess.TimeoutExpired:
        subprocess.run(
            ["docker", "rm", "-f", name],
            text=True,
            capture_output=True,
            timeout=15,
            check=False,
        )
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--workdir", required=True, type=Path)
    parser.add_argument("--timeout-seconds", required=True, type=float)
    parser.add_argument("--cpu-cores", required=True, type=int)
    parser.add_argument("--memory-gb", required=True, type=int)
    parser.add_argument("command")
    args = parser.parse_args()
    try:
        done = run_sandboxed(
            args.image,
            args.workdir,
            args.command,
            args.timeout_seconds,
            args.cpu_cores,
            args.memory_gb,
        )
    except subprocess.TimeoutExpired:
        return 124
    print(done.stdout, end="")
    print(done.stderr, end="", file=os.sys.stderr)
    return done.returncode


if __name__ == "__main__":
    raise SystemExit(main())
