# Diffcipline benchmark

This directory contains the public benchmark used to test Diffcipline's behavioral claims.

The corpus is intentionally small, deterministic, and adversarial to marketing claims. It includes tasks where minimality should help and one task where the correct action is to make no code change.

## Frozen fixture set

| ID | Class | Intent |
| --- | --- | --- |
| `f01-shared-root-cause` | shared root-cause bug | fix one policy boundary instead of copies |
| `f02-stdlib-query` | standard-library solution | prefer a native parser over custom code or dependencies |
| `f03-dependency-temptation` | dependency temptation | use current platform capability before adding a package |
| `f04-refactor-preserve` | behavior-preserving refactor | consolidate one repeated rule without broad cleanup |
| `f05-security-boundary` | security boundary | preserve containment against traversal and symlink escape |
| `f06-already-minimal` | no-op / already correct | verify first and leave correct code unchanged |

Every task includes a user-facing `TASK.md`, a machine-readable `manifest.json`, and a disposable repository snapshot under `repo/`. The agent never receives the manifest or benchmark harness inside its working repository.

## Validate the fixture corpus

```bash
python benchmarks/harness/validate_fixtures.py
```

The validator confirms that fixtures expected to start broken actually fail and that the already-correct fixture starts green.

## Scoring contract

`benchmarks/harness/score_run.py` records evidence rather than an opaque quality score: objective correctness, protected-file integrity, diff integrity, changed files, added/deleted lines, unrelated churn, dependency-file churn, and transcript-observed verification.

A run passes only when correctness, protected-file integrity, and `git diff --check` pass. Minimality metrics remain separate observations; fewer lines never override correctness.

Execution arms and published results are added only after this corpus is merged and therefore frozen.
