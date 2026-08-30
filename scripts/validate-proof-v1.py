#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "proof-v1.json"

schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
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
properties = list(schema["properties"])
if list(proof) != properties:
    raise SystemExit(f"proof field order mismatch: {list(proof)} != {properties}")

missing = [field for field in schema["required"] if field not in proof]
if missing:
    raise SystemExit(f"missing required proof fields: {missing}")
if proof["schema"] != schema["$id"] or proof["schema_version"] != "1.0":
    raise SystemExit("proof schema identity mismatch")
if proof["verdict"] not in {"PASS", "REVIEW", "FAIL"}:
    raise SystemExit("invalid verdict")
if proof["policy"]["mode"] not in {"default", "repository", "enterprise"}:
    raise SystemExit("invalid policy mode")
if not isinstance(proof["policy"]["sources"], list):
    raise SystemExit("policy sources must be an array")
for item in proof["verification"]:
    if item["state"] not in {"PASS", "FAIL", "NOT RUN"}:
        raise SystemExit("invalid verification state")

print("proof-v1 schema contract PASS")
