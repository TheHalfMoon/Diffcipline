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

Phase E qualification T240–T243 merged at `35b3a0de5e17d1ce2a20ab3ffdc224d440313363`. Its canonical qualification push `33261050250` was SUCCESS and produced `v0.3-harness-qualification` artifact `9717258339`; the artifact proved `PASS`, 24 deterministic matrix rows, `private_credentials_required=false`, `comparative_model_execution=false`, and preservation of the frozen v0.1 benchmark blobs.

Phase E guarded-entry T244 and the final T245 merge boundary merged at `3be4df7e19b7fd4410bb1127fdd91da9d2f27fc8`. PR #49 exact head `e1722417ec64200c0d218c1ba3a84d33c9fd247d` passed `benchmark-v0.3-reference` `33262020518`, `benchmark-v0.3-qualification` `33262020492`, `benchmark-fixtures` `33262020534`, and `ci` `33262020505`. Exact post-merge push runs `benchmark-v0.3-qualification` `33262094960`, `benchmark-fixtures` `33262095055`, and `ci` `33262094948` were SUCCESS. Canonical qualification artifact `9717538620` has digest `sha256:c8a5ccc984d86d58f18fc495c1d485b42434f4e51f12b8a03dde305655616a8d` and records repository revision `3be4df7e19b7fd4410bb1127fdd91da9d2f27fc8`, `PASS`, 24 rows, no private credentials, and no comparative model execution.

The guarded reference workflow intentionally has no push trigger. Its PR validation proves the owner-command entry contract without executing a model. Comparative execution remains available only through `/run-v0.3-reference <canonical-main-sha>` after the Phase F entry gates are canonical.

## Active frontier

T250–T251 are the immediate Phase F authority unit: freeze the exact secret-free reference executor/runtime/model/treatment provenance and prove that task revision, permissions, prompt suffix, timeout, and resource constraints are identical across treatment arms.

Before T252/T253 execution is enabled, the real experiment path must enforce the declared workspace/network/Git-push containment rather than merely recording those permissions in configuration. Baseline and eligible comparison skills must execute before Diffcipline under the canonical deterministic order `baseline → karpathy → ponytail → diffcipline`.

No comparative result may be selectively rerun, dropped, or rewritten because it is unfavorable. T252/T253 remain unauthorized until T250/T251 are canonical and the guarded workflow's execution body has passed exact-head and post-merge verification.
