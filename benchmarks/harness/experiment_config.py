#!/usr/bin/env python3
import argparse
import copy
import json
import re
from pathlib import Path

ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
HEX40_RE = re.compile(r"^[0-9a-f]{40}$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
ADAPTER_KINDS = {"local-openai-tool-loop"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def require_keys(value: dict, required: set[str], context: str) -> None:
    missing = required - value.keys()
    require(not missing, f"{context}: missing {', '.join(sorted(missing))}")


def stable_id(value: object, context: str) -> str:
    require(isinstance(value, str) and bool(ID_RE.fullmatch(value)), f"{context}: invalid id")
    return value


def positive_int(value: object, context: str) -> None:
    require(isinstance(value, int) and not isinstance(value, bool) and value > 0, f"{context}: must be a positive integer")


def validate_source(source: object, context: str) -> None:
    require(isinstance(source, dict), f"{context}: source must be an object")
    require_keys(source, {"repository", "revision", "path", "digest"}, context)
    require(isinstance(source["repository"], str) and source["repository"].count("/") == 1, f"{context}: invalid repository")
    require(isinstance(source["revision"], str) and HEX40_RE.fullmatch(source["revision"]), f"{context}: invalid revision")
    require(isinstance(source["path"], str) and source["path"] and not source["path"].startswith("/"), f"{context}: invalid path")
    digest = source["digest"]
    require(isinstance(digest, dict) and digest.get("algorithm") == "git-blob-sha1", f"{context}: unsupported digest")
    require(isinstance(digest.get("value"), str) and HEX40_RE.fullmatch(digest["value"]), f"{context}: invalid digest value")


def validate_executor(executor: object, ids: set[str]) -> None:
    require(isinstance(executor, dict), "executor must be an object")
    require_keys(executor, {"id", "adapter_kind", "runtime", "model", "tools", "permissions", "resource_limits"}, "executor")
    executor_id = stable_id(executor["id"], "executor")
    require(executor_id not in ids, f"duplicate executor id: {executor_id}")
    ids.add(executor_id)
    require(executor["adapter_kind"] in ADAPTER_KINDS, f"{executor_id}: unsupported adapter kind")
    runtime = executor["runtime"]
    require(isinstance(runtime, dict), f"{executor_id}: runtime must be an object")
    require_keys(runtime, {"name", "release", "revision", "sha256"}, f"{executor_id}.runtime")
    require(all(isinstance(runtime[key], str) and runtime[key] for key in ("name", "release")), f"{executor_id}: invalid runtime identity")
    require(HEX40_RE.fullmatch(runtime["revision"]) is not None, f"{executor_id}: invalid runtime revision")
    require(HEX64_RE.fullmatch(runtime["sha256"]) is not None, f"{executor_id}: invalid runtime sha256")
    model = executor["model"]
    require(isinstance(model, dict), f"{executor_id}: model must be an object")
    require_keys(model, {"id", "repository", "revision", "sha256"}, f"{executor_id}.model")
    require(all(isinstance(model[key], str) and model[key] for key in ("id", "repository")), f"{executor_id}: invalid model identity")
    require(HEX40_RE.fullmatch(model["revision"]) is not None, f"{executor_id}: invalid model revision")
    require(HEX64_RE.fullmatch(model["sha256"]) is not None, f"{executor_id}: invalid model sha256")
    require(executor["tools"] == ["bash"], f"{executor_id}: tools must be ['bash']")
    permissions = executor["permissions"]
    require(permissions == {"network_tools": "denied", "git_push": "denied", "workspace": "disposable-only"}, f"{executor_id}: unsafe permissions")
    limits = executor["resource_limits"]
    require(isinstance(limits, dict), f"{executor_id}: resource_limits must be an object")
    require_keys(limits, {"cpu_cores", "memory_gb", "storage_gb", "per_task_timeout_seconds"}, f"{executor_id}.resource_limits")
    for key in ("cpu_cores", "memory_gb", "storage_gb", "per_task_timeout_seconds"):
        positive_int(limits[key], f"{executor_id}.{key}")


def validate_treatment(treatment: object, ids: set[str]) -> None:
    require(isinstance(treatment, dict), "treatment must be an object")
    require_keys(treatment, {"id", "kind"}, "treatment")
    treatment_id = stable_id(treatment["id"], "treatment")
    require(treatment_id not in ids, f"duplicate treatment id: {treatment_id}")
    ids.add(treatment_id)
    require(treatment["kind"] in {"none", "skill"}, f"{treatment_id}: unsupported treatment kind")
    if treatment["kind"] == "none":
        require(treatment_id == "baseline" and set(treatment) == {"id", "kind"}, "baseline must be the sole untreated arm")
    else:
        validate_source(treatment.get("source"), treatment_id)


def validate_config(config: object) -> dict:
    require(isinstance(config, dict), "config must be an object")
    require_keys(config, {"schema_version", "benchmark_version", "fixture_revision", "prompt_suffix", "executors", "treatments"}, "config")
    require(config["schema_version"] == 1, "unsupported schema_version")
    require(config["benchmark_version"] == "v0.3", "benchmark_version must be v0.3")
    require(isinstance(config["fixture_revision"], str) and HEX40_RE.fullmatch(config["fixture_revision"]), "invalid fixture_revision")
    require(isinstance(config["prompt_suffix"], str) and config["prompt_suffix"].strip(), "prompt_suffix must be non-empty")
    require(isinstance(config["executors"], list) and config["executors"], "executors must be non-empty")
    require(isinstance(config["treatments"], list) and config["treatments"], "treatments must be non-empty")
    executor_ids: set[str] = set()
    treatment_ids: set[str] = set()
    for executor in config["executors"]:
        validate_executor(executor, executor_ids)
    for treatment in config["treatments"]:
        validate_treatment(treatment, treatment_ids)
    require("baseline" in treatment_ids and "diffcipline" in treatment_ids, "baseline and diffcipline treatments are required")
    return config


def normalize_config(config: object) -> dict:
    value = copy.deepcopy(validate_config(config))
    value["executors"] = sorted(value["executors"], key=lambda item: item["id"])
    value["treatments"] = sorted(value["treatments"], key=lambda item: item["id"])
    return value


def serialize_normalized(config: object) -> str:
    return json.dumps(normalize_config(config), indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path)
    parser.add_argument("--normalized", action="store_true")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    output = serialize_normalized(config) if args.normalized else "valid\n"
    print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
