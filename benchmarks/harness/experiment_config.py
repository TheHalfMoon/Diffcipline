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
SANDBOX_CONTRACT = {
    "kind": "docker-python-v1",
    "image": "python:3.12.11-slim-bookworm@sha256:519591d6871b7bc437060736b9f7456b8731f1499a57e22e6c285135ae657bf7",
    "network": "none",
    "root_filesystem": "read-only",
    "workspace_mount": "read-write-only",
    "capabilities": "drop-all",
    "no_new_privileges": True,
}


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


def https_url(value: object, context: str) -> None:
    require(isinstance(value, str) and value.startswith("https://") and " " not in value, f"{context}: invalid https URL")


def repository_id(value: object, context: str) -> None:
    require(isinstance(value, str) and value.count("/") == 1 and all(value.split("/")), f"{context}: invalid repository")


def validate_source(source: object, context: str) -> None:
    require(isinstance(source, dict), f"{context}: source must be an object")
    require_keys(source, {"repository", "revision", "path", "digest"}, context)
    repository_id(source["repository"], context)
    require(isinstance(source["revision"], str) and HEX40_RE.fullmatch(source["revision"]), f"{context}: invalid revision")
    require(isinstance(source["path"], str) and source["path"] and not source["path"].startswith("/"), f"{context}: invalid path")
    digest = source["digest"]
    require(isinstance(digest, dict) and digest.get("algorithm") == "git-blob-sha1", f"{context}: unsupported digest")
    require(isinstance(digest.get("value"), str) and HEX40_RE.fullmatch(digest["value"]), f"{context}: invalid digest value")


def validate_runtime(runtime: object, executor_id: str) -> None:
    context = f"{executor_id}.runtime"
    require(isinstance(runtime, dict), f"{context}: runtime must be an object")
    require_keys(runtime, {"name", "repository", "release", "revision", "download_url", "sha256", "base_url", "server_args", "chat_template"}, context)
    require(all(isinstance(runtime[key], str) and runtime[key] for key in ("name", "release")), f"{context}: invalid runtime identity")
    repository_id(runtime["repository"], context)
    require(isinstance(runtime["revision"], str) and HEX40_RE.fullmatch(runtime["revision"]), f"{context}: invalid runtime revision")
    https_url(runtime["download_url"], f"{context}.download_url")
    require(isinstance(runtime["sha256"], str) and HEX64_RE.fullmatch(runtime["sha256"]), f"{context}: invalid runtime sha256")
    require(isinstance(runtime["base_url"], str) and runtime["base_url"].startswith("http://127.0.0.1:"), f"{context}: base_url must be loopback")
    require(isinstance(runtime["server_args"], list) and runtime["server_args"] and all(isinstance(item, str) and item for item in runtime["server_args"]), f"{context}: invalid server_args")
    template = runtime["chat_template"]
    require(isinstance(template, dict), f"{context}.chat_template: must be an object")
    require_keys(template, {"revision", "path", "digest"}, f"{context}.chat_template")
    require(template["revision"] == runtime["revision"], f"{context}.chat_template: revision must match runtime")
    require(isinstance(template["path"], str) and template["path"] and not template["path"].startswith("/"), f"{context}.chat_template: invalid path")
    digest = template["digest"]
    require(isinstance(digest, dict) and digest.get("algorithm") == "git-blob-sha1", f"{context}.chat_template: unsupported digest")
    require(isinstance(digest.get("value"), str) and HEX40_RE.fullmatch(digest["value"]), f"{context}.chat_template: invalid digest")


def validate_model(model: object, executor_id: str) -> None:
    context = f"{executor_id}.model"
    require(isinstance(model, dict), f"{context}: model must be an object")
    require_keys(model, {"id", "repository", "revision", "file", "download_url", "sha256", "quantization", "license"}, context)
    require(all(isinstance(model[key], str) and model[key] for key in ("id", "file", "quantization", "license")), f"{context}: invalid model identity")
    repository_id(model["repository"], context)
    require(isinstance(model["revision"], str) and HEX40_RE.fullmatch(model["revision"]), f"{context}: invalid model revision")
    https_url(model["download_url"], f"{context}.download_url")
    require(isinstance(model["sha256"], str) and HEX64_RE.fullmatch(model["sha256"]), f"{context}: invalid model sha256")


def validate_executor(executor: object, ids: set[str]) -> None:
    require(isinstance(executor, dict), "executor must be an object")
    require_keys(executor, {"id", "adapter_kind", "runtime", "model", "tools", "permissions", "resource_limits", "sandbox"}, "executor")
    executor_id = stable_id(executor["id"], "executor")
    require(executor_id not in ids, f"duplicate executor id: {executor_id}")
    ids.add(executor_id)
    require(executor["adapter_kind"] in ADAPTER_KINDS, f"{executor_id}: unsupported adapter kind")
    validate_runtime(executor["runtime"], executor_id)
    validate_model(executor["model"], executor_id)
    require(executor["tools"] == ["bash"], f"{executor_id}: tools must be ['bash']")
    permissions = executor["permissions"]
    require(permissions == {"network_tools": "denied", "git_push": "denied", "workspace": "disposable-only"}, f"{executor_id}: unsafe permissions")
    require(executor["sandbox"] == SANDBOX_CONTRACT, f"{executor_id}: unsafe sandbox contract")
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
