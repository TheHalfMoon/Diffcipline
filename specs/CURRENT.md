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

Phase C T220–T225 became canonical at `8e84a013296ae6cf62d41f68068eb1094c422b2d` with post-merge `benchmark-fixtures` `33257939873`, `ci` `33257939894`, `skills-compat` `33257939867`, and `release` `33257939883` SUCCESS. Legacy `benchmark-arms` run `33257939909` also succeeded, but it is regression-only evidence and cannot satisfy v0.3 comparative-experiment tasks or alter frozen v0.1 results.

Phase D T230–T235 became canonical at `b4900b45d4ff3cb2e26ef3f4134b0d72087672a9`. PR #46 exact head `927e37cbbaec7db5dfccbd32002f71181c081d37` passed `benchmark-fixtures` `33260403823` and `ci` `33260403827`; after merge, exact canonical push runs `benchmark-fixtures` `33260476350` and `ci` `33260476379` were SUCCESS.

## Active frontier

T240–T245 are the active Phase E unit: qualify the public harness without private credentials, run deterministic CI checks for config/adapters/matrix/evidence completeness, preserve the frozen v0.1 scorer/fixture boundary, and define an explicit real-experiment workflow that cannot run on ordinary pull requests.

No real comparative v0.3 experiment is authorized before T245 becomes canonical. Contract fixtures and deterministic adapters may qualify the harness, but their outputs are not model-comparison evidence.
