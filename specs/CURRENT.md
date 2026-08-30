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

Phase F containment and pinned execution-body implementation merged through PR #51 and PR #52. PR #51 exact head `82b701e43f3d64b57c9fc8da266cdc33489cdaf7` passed the reference, fixture, qualification, CI, and legacy regression workflows; its merge commit was `f1f41f52a732230b39ac8cba082db262a0d58c9e`. PR #52 exact head `b089c4b06c41aa62848bf8a5ae9f5eb420f5d0f3` passed `benchmark-v0.3-reference` `33264366591`, `benchmark-v0.3-qualification` `33264366617`, `benchmark-fixtures` `33264366590`, and `ci` `33264366589`; its merge commit is canonical `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea`.

On `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea`, post-merge `benchmark-fixtures` `33264509821`, `benchmark-v0.3-qualification` `33264509832`, and `ci` `33264510009` were SUCCESS. Qualification artifact `9718225574`, digest `sha256:2d9c782799b376b6c61ccb617941e4f7dbc6d93a1d7efa757c9d3794f2b2bd94`, proves the exact 24-row contract, pinned sandbox and resource limits, denied network, read-only root, disposable workspace write boundary, absent Docker socket, no credential exposure, and `comparative_model_execution=false`. Exact details are recorded in `specs/003-evidence-benchmark/phase-f-entry-evidence.md`.

T250–T251 became canonical at `234f007dc8765f7b7649ada7d7d1d00ae4c12538`, establishing the exact one-shot public reference-experiment boundary.

## Accepted v0.3 reference experiment

Canonical workflow run `33269484561` (#16) executed exactly once against target `234f007dc8765f7b7649ada7d7d1d00ae4c12538` after qualification run `33269349342`. It completed `SUCCESS` and produced raw results artifact `9720290597`, digest `sha256:dcad221a52e110a34198109ac31bfe164e2ac47610e78b83b9d98f17102c3218`, plus reservation artifact `9719653684`, digest `sha256:f63e381cb199a064b875cdaf25eba614f3ea9b38048cd20bfbc18a689d6e28b7`.

T254 inspection accepted the exact artifact without a rerun: all 24 rows and every required run bundle are present; base commits and comparison contracts match across treatments; pinned runtime/model/treatment/sandbox provenance matches; qualification and containment are `PASS`; and the manifest preserves 12 `included`, 12 `failed`, 0 `timed_out`, and 0 `excluded` rows.

The frozen scorer remains unchanged. Test execution generated Python `__pycache__` files that the scorer counted as changed/unrelated/protected paths, producing `0/6` scorer-pass for every treatment even though every treatment is `1/6` task-correct and all textual patches are empty. This is a published limitation, not a post-hoc justification for changing the scorer or rerunning tasks.

The artifact-internal pre-packaging checksum ledger contains 463 entries. The downloaded Actions artifact contains 295 of those paths and all 295 match; the 168 omitted paths are hidden `.git` metadata from duplicate ephemeral work repositories. No required transcript, stdout, stderr, score, patch, status, metadata, resulting workspace, reservation, qualification, validation, or provenance record is missing.

## Active frontier

T252–T255 are complete by accepted experiment evidence. T260–T262 are implemented on the current publication candidate through `benchmarks/results/v0.3/`, `README.md`, and the reconciled Spec 003 ledger.

The immediate frontier is **T263**: the exact final publication candidate must pass repository CI, v0.3 benchmark qualification, skills compatibility, and release-candidate gates on one exact head. T263 remains open until those machine-observed gates succeed on that head.

After T263, reconcile all valid review findings and threads, verify canonical `main` did not move unexpectedly, and merge only with an expected-head guard. T264 requires exact post-merge gates on the resulting canonical `main`. T265 must be recorded separately only after T264 is machine-observed; Spec 003 cannot be claimed `COMPLETE_CANONICAL` before that completion record itself becomes canonical.

No v0.3 release tag and no v1.0 implementation are authorized by this candidate.
