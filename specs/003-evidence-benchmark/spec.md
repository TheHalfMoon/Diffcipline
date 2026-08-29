# Spec 003 — Evidence Benchmark

## Status

`PLANNING`

## Roadmap authority

The canonical README defines v0.3 as **Evidence benchmark** with two product goals:

1. a public multi-agent benchmark harness;
2. reproducible baselines against unassisted agents and other skills.

This specification turns those goals into a deterministic repository contract. It does not authorize v1.0 work, a v0.3 release tag, or marketing claims unsupported by published evidence.

## Problem

The existing benchmark has a frozen six-task corpus, deterministic objective scorer, one repository-local agent loop, and a pinned v0.1 experiment. `run_arm.py` currently binds each treatment arm directly to `local_agent.py`, one model, and one base URL. That structure cannot distinguish executor identity from treatment identity and is not yet a general public multi-agent harness.

## Product contract

### Executor profiles

A benchmark executor profile identifies how one coding-agent runtime is invoked. A profile must record a stable ID, adapter kind, command/runtime identity, model identity when applicable, version or revision evidence, tool permissions, environment requirements, and resource limits.

Executor selection and treatment selection are independent dimensions. A treatment must never silently change the executor, model, task revision, tool permissions, timeout, or resource limits.

### Treatment arms

For every qualified executor profile, the harness supports at least:

- `baseline`: no behavioral skill;
- zero or more comparison skills whose exact source revision and content digest are recorded;
- `diffcipline`: the exact Diffcipline skill revision under test.

A comparison is valid only when task, fixture revision, executor profile, model, permissions, prompt suffix, timeout, and resource limits match across arms.

### Adapter boundary

The orchestrator invokes an executor through one explicit adapter contract. The adapter receives a prepared repository, user task, optional treatment file, timeout, and transcript/output destinations. It returns process evidence only; it does not score the result.

Scoring remains a separate deterministic step using repository state and fixture manifests.

### Evidence schema

Every task run must preserve enough machine evidence to reproduce and audit it:

- executor profile and treatment identity;
- repository and fixture revision;
- model/runtime revision when applicable;
- start time, duration, timeout, and exit status;
- stdout, stderr, transcript when available, patch, status, and resulting workspace;
- deterministic scorer output;
- hashes for treatment and adapter inputs that affect execution.

Every experiment must publish a manifest that enumerates included and excluded runs. Exclusions require explicit reasons and remain visible.

### Reporting

Reports keep correctness and integrity separate from minimality metrics. Results are stratified by executor and treatment; they are not pooled as if different executors were interchangeable replicates.

No correctness advantage, regression advantage, or productivity claim may be made unless the published evidence supports it. Losing metrics, timeouts, parser/tool failures, unavailable token/cost data, and negative results remain visible.

## Compatibility and preservation

- Existing v0.1 raw evidence, report, manifest, checksums, frozen fixture revision, and invalid-run exclusion remain unchanged.
- Existing fixture manifests and objective scoring semantics are not rewritten merely to improve benchmark results.
- The harness remains Python standard-library only unless a separate governance change demonstrates a necessary dependency.
- Core Diffcipline CLI behavior is out of scope.

## Canonical qualification

The repository must be able to qualify the public harness without private credentials. Credential-dependent executor profiles may be documented as optional, but they cannot be required for canonical CI qualification or used as sole evidence for v0.3 completion.

At least one fully pinned, secret-free reference executor must pass end-to-end harness qualification. The adapter architecture must support multiple executor profiles without embedding executor-specific logic into the scorer.

## Non-goals

- semantic or LLM-as-judge correctness scoring;
- changing a task after observing an arm result to improve that arm;
- selective reruns or result filtering;
- claiming treatment effects from unmatched executor/model configurations;
- replacing the unfavorable v0.1 result;
- introducing network access or Git push inside benchmark workspaces;
- authorizing v1.0 enterprise policy or stable proof-schema work.

## Completion rule

Spec 003 is `COMPLETE_CANONICAL` only after its task ledger is complete, the public harness and reproducibility evidence are merged to canonical `main`, all required exact-head and post-merge gates succeed, and the final evidence record itself is canonical.
