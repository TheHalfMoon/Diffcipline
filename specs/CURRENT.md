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

Spec 001 reached `COMPLETE_CANONICAL` at `d74ed5f8789fb255e24f124e3283939cdc080cd0`. The fixed `v0.1.0` tag remains directly at `ab434ae114b5f11ea9eb882bf572831dc7634531`; Release ID `378936458` is immutable.

The canonical v0.1 benchmark remains intentionally unfavorable: baseline, Karpathy, Ponytail, and Diffcipline each scored `1/6`; all four arms changed zero files; Diffcipline was slowest; and no correctness advantage is supported. Invalid run `33195457215` remains excluded.

## Completed Spec 002 / v0.2

Spec 002 reached `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. Final post-merge `ci` `33256238377`, `skills-compat` `33256238390`, and `release` `33256238367` were SUCCESS. No `v0.2.0` tag was authorized or created.

## Spec 003 authority and canonical progress

The README defines v0.3 as **Evidence benchmark**: a public multi-agent benchmark harness with reproducible baselines against unassisted agents and other skills. Spec 003 preserves frozen v0.1 evidence and forbids semantic/LLM-as-judge scoring, selective reruns, hidden exclusions, v1.0 work, and a v0.3 release tag.

Planning T200–T203 became canonical at `c392d372564b55cc7d55aee8bed1b2641dee6820` with post-merge `ci` `33256584608`, `skills-compat` `33256584575`, and `release` `33256584593` SUCCESS.

Phase B T210–T215 became canonical at `5726c54f1b807a8d0976d71308c61cf70687d621` with post-merge `benchmark-fixtures` `33257309999`, `ci` `33257309939`, `skills-compat` `33257309945`, and `release` `33257309947` SUCCESS.

## Active frontier

T220–T225 are the active Phase C unit: move arm execution behind a process-level adapter contract, preserve the existing local OpenAI-compatible loop as the reference adapter, add a deterministic qualification-only contract adapter, preserve process/treatment evidence, and cover success/failure/timeout/containment paths.

T230 matrix work remains blocked until T220–T225 pass exact-head gates, review reconciliation, canonical merge, and exact post-merge verification.

No real comparative v0.3 experiment is authorized before T245. A legacy v0.1 `benchmark-arms` run automatically triggered by a `run_arm.py` change is regression evidence only and cannot count toward v0.3 comparative execution or alter the frozen v0.1 result.
