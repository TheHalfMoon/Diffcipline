#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "proof-v1.json"
schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def validate(proof):
    properties = list(schema["properties"])
    if list(proof) != properties:
        raise ValueError(f"proof field order mismatch: {list(proof)} != {properties}")
    missing = [field for field in schema["required"] if field not in proof]
    if missing:
        raise ValueError(f"missing required proof fields: {missing}")
    if proof["schema"] != schema["$id"] or proof["schema_version"] != "1.0":
        raise ValueError("proof schema identity mismatch")
    if proof["verdict"] not in {"PASS", "REVIEW", "FAIL"}:
        raise ValueError("invalid verdict")
    if proof["policy"]["mode"] not in {"default", "repository", "enterprise"}:
        raise ValueError("invalid policy mode")
    if not isinstance(proof["policy"]["sources"], list):
        raise ValueError("policy sources must be an array")
    for item in proof["verification"]:
        if item["state"] not in {"PASS", "FAIL", "NOT RUN"}:
            raise ValueError("invalid verification state")


proc = subprocess.run(
    ["cargo", "run", "--quiet", "--locked", "--package", "diffcipline", "--", "check", "--json"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
)
if proc.returncode not in (0, 1, 2):
    raise SystemExit(f"diffcipline check failed unexpectedly: {proc.returncode}\n{proc.stderr}")

proof = json.loads(proc.stdout)
validate(proof)

incompatible = dict(proof)
incompatible["schema_version"] = "2.0"
try:
    validate(incompatible)
except ValueError:
    pass
else:
    raise SystemExit("validator accepted incompatible schema version")

print("proof-v1 schema contract PASS")
