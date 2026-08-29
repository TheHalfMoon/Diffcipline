# Current specification

Active: [`003-evidence-benchmark`](003-evidence-benchmark/spec.md)

Status: `IMPLEMENTATION`

## Canonical read order

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. `README.md` roadmap and benchmark doctrine
4. this file
5. `specs/003-evidence-benchmark/spec.md`
6. `specs/003-evidence-benchmark/plan.md`
7. `specs/003-evidence-benchmark/tasks.md`
8. `specs/003-evidence-benchmark/execution-frontier.md`
9. `benchmarks/PROTOCOL.md`
10. `benchmarks/README.md`
11. frozen `benchmarks/run-config.json`
12. benchmark harness, scorer, and workflows relevant to the active task.

Live GitHub/repository truth overrides every recorded SHA below.

## Completed Spec 001 / v0.1

Spec 001 reached `COMPLETE_CANONICAL` at `d74ed5f8789fb255e24f124e3283939cdc080cd0`.

The fixed `v0.1.0` tag remains directly at `ab434ae114b5f11ea9eb882bf572831dc7634531`. Release ID `378936458` is immutable.

The canonical v0.1 benchmark remains intentionally unfavorable: baseline, Karpathy, Ponytail, and Diffcipline each scored `1/6`; all four arms changed zero files; Diffcipline was slowest by observed wall-clock time; and no correctness advantage is supported. Invalid run `33195457215` remains excluded.

## Completed Spec 002 / v0.2

Spec 002 reached `COMPLETE_CANONICAL` on canonical `main` at:

`0a6513aa17c90840a5024c62684d042571d431ed`

Final canonical post-merge evidence on that exact commit:

- `ci` `33256238377`: SUCCESS;
- `skills-compat` `33256238390`: SUCCESS;
- `release` `33256238367`: SUCCESS.

Spec 002 delivered deterministic expected/forbidden scope proof, R0–R3 verification profiles, additive human/JSON proof evidence, and read-only GitHub job-summary annotation. T150–T154 are complete in its canonical task ledger.

No `v0.2.0` tag was authorized or created.

## Spec 003 authority

The canonical README roadmap defines v0.3 as **Evidence benchmark** with two goals:

1. a public multi-agent benchmark harness;
2. reproducible baselines against unassisted agents and other skills.

The existing repository already has a frozen six-task corpus, an objective scorer, a pinned v0.1 local runtime/model experiment, and a repository-local agent loop. The active gap is an executor-independent public harness and evidence contract that separates executor identity from treatment identity.

Spec 003 preserves the frozen v0.1 evidence boundary and does not authorize semantic/LLM-as-judge scoring, selective reruns, hidden exclusions, v1.0 work, or a v0.3 release tag.

## Canonical planning evidence

Spec 003 planning authority reached canonical `main` at:

`c392d372564b55cc7d55aee8bed1b2641dee6820`

Post-merge runs on that exact commit:

- `ci` `33256584608`: SUCCESS;
- `skills-compat` `33256584575`: SUCCESS;
- `release` `33256584593`: SUCCESS.

T200–T203 are therefore canonical.

## Active frontier

T210–T215 are the active Phase B unit: introduce and validate a versioned v0.3 experiment configuration that separates executor profiles from treatment arms while leaving frozen v0.1 `benchmarks/run-config.json` unchanged.

T220 adapter work remains blocked until T210–T215 pass exact-head gates, review reconciliation, canonical merge, and exact post-merge verification.

No real comparative v0.3 experiment is authorized before T245. Contract fixtures and deterministic test adapters may qualify the harness before that boundary, but their outputs are not comparative model evidence.
