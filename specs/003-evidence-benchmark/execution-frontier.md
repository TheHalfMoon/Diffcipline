# Execution frontier — Spec 003

Live GitHub/repository truth overrides this snapshot.

## Canonical authority chain

Read in this order before acting:

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. `README.md` roadmap and benchmark doctrine
4. `specs/CURRENT.md`
5. `specs/003-evidence-benchmark/spec.md`
6. `specs/003-evidence-benchmark/plan.md`
7. `specs/003-evidence-benchmark/tasks.md`
8. this file
9. `benchmarks/PROTOCOL.md`
10. `benchmarks/README.md`
11. frozen `benchmarks/run-config.json`
12. benchmark harness/scorer/workflows relevant to the active task.

## Preserved canonical history

Spec 001 / v0.1 and Spec 002 / v0.2 are complete. The immutable `v0.1.0` tag remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

The canonical v0.1 benchmark remains unfavorable: every arm scored `1/6`, all arms changed zero files, Diffcipline was slowest, and no correctness advantage is supported. The invalid run `33195457215` remains excluded.

Do not rewrite v0.1 evidence, fixtures, scorer history, or published limitations to improve later results.

## Canonical Spec 003 evidence

Planning T200–T203 became canonical at `c392d372564b55cc7d55aee8bed1b2641dee6820` with post-merge `ci` `33256584608`, `skills-compat` `33256584575`, and `release` `33256584593` all SUCCESS.

Phase B T210–T215 became canonical at `5726c54f1b807a8d0976d71308c61cf70687d621` with post-merge `benchmark-fixtures` `33257309999`, `ci` `33257309939`, `skills-compat` `33257309945`, and `release` `33257309947` all SUCCESS.

Phase C T220–T225 became canonical at `8e84a013296ae6cf62d41f68068eb1094c422b2d`. Post-merge `benchmark-fixtures` `33257939873`, `ci` `33257939894`, `skills-compat` `33257939867`, and `release` `33257939883` all succeeded. Legacy `benchmark-arms` run `33257939909` also succeeded, but it is regression-only evidence and cannot satisfy v0.3 T250–T255 or alter frozen v0.1 results.

Phase D T230–T235 became canonical at `b4900b45d4ff3cb2e26ef3f4134b0d72087672a9`. PR #46 exact head `927e37cbbaec7db5dfccbd32002f71181c081d37` passed `benchmark-fixtures` `33260403823` and `ci` `33260403827`; exact post-merge `benchmark-fixtures` `33260476350` and `ci` `33260476379` also succeeded.

Phase E T240–T243 qualification implementation merged at `35b3a0de5e17d1ce2a20ab3ffdc224d440313363`. Canonical `benchmark-v0.3-qualification` run `33261050250` succeeded and emitted artifact `9717258339`, proving a secret-free 24-row qualification path with no comparative model execution while preserving the frozen v0.1 fixture/preparer/scorer boundary.

Phase E T244 guarded reference entry and the T245 merge boundary merged at `3be4df7e19b7fd4410bb1127fdd91da9d2f27fc8`. PR #49 exact head `e1722417ec64200c0d218c1ba3a84d33c9fd247d` passed `benchmark-v0.3-reference` `33262020518`, `benchmark-v0.3-qualification` `33262020492`, `benchmark-fixtures` `33262020534`, and `ci` `33262020505`. Exact post-merge `benchmark-v0.3-qualification` `33262094960`, `benchmark-fixtures` `33262095055`, and `ci` `33262094948` succeeded. Qualification artifact `9717538620` records 24 rows, no private credentials, no comparative model execution, and the frozen v0.1 boundary.

## Phase F entry evidence

Containment implementation PR #51 exact head `82b701e43f3d64b57c9fc8da266cdc33489cdaf7` passed:

- `benchmark-v0.3-reference` `33263875157`: SUCCESS;
- `benchmark-fixtures` `33263875156`: SUCCESS;
- `benchmark-v0.3-qualification` `33263875174`: SUCCESS;
- `ci` `33263875162`: SUCCESS;
- legacy `benchmark-arms` `33263875194`: SUCCESS and regression-only.

PR #51 merged as `f1f41f52a732230b39ac8cba082db262a0d58c9e`. Its qualification artifact `9718040977`, digest `sha256:f982a83cf9bfbff45ccbb5d7a1862e973e343de7845de3782161bcfff6ce71a6`, proved the pinned Docker containment on the exact head without comparative model execution.

Pinned execution-body PR #52 exact head `b089c4b06c41aa62848bf8a5ae9f5eb420f5d0f3` passed:

- `benchmark-v0.3-reference` `33264366591`: SUCCESS;
- `benchmark-v0.3-qualification` `33264366617`: SUCCESS;
- `benchmark-fixtures` `33264366590`: SUCCESS;
- `ci` `33264366589`: SUCCESS.

PR #52 had no submitted reviews or inline review comments and merged as canonical `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea`.

Exact post-merge evidence on `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea` is:

- `benchmark-fixtures` `33264509821`: SUCCESS;
- `benchmark-v0.3-qualification` `33264509832`: SUCCESS;
- `ci` `33264510009`: SUCCESS.

Canonical qualification artifact `9718225574`, digest `sha256:2d9c782799b376b6c61ccb617941e4f7dbc6d93a1d7efa757c9d3794f2b2bd94`, records the exact canonical revision, result `PASS`, 24 matrix rows, the pinned runtime/model/resource/sandbox contract, `private_credentials_required=false`, `comparative_model_execution=false`, network denied, read-only root, verified workspace write, absent Docker socket, and no private credential exposure.

The detailed ledger is `specs/003-evidence-benchmark/phase-f-entry-evidence.md`.

## Current benchmark truth

The reference experiment contract is now fully pinned and executable through one guarded owner-command path. The runtime/model/treatment source lineage is cross-checked against frozen v0.1 source provenance before execution. The agent's bash tool is contained in a digest-pinned Docker image with network disabled, a read-only root filesystem, an isolated temporary filesystem, no Docker socket, no inherited GitHub credentials, and only the disposable fixture workspace writable.

The execution workflow reserves a canonical target SHA before runtime/model setup, rejects duplicate target execution, verifies exact successful qualification evidence for the target, downloads and checksum-verifies every pinned runtime/model/treatment input, executes one 24-row matrix in canonical treatment order, and uploads all raw evidence even when runs fail or time out.

No v0.3 comparative model execution has yet been accepted or published.

## Immediate frontier

This evidence change records T250–T251 as complete. They become canonical only after this branch is merged and its exact post-merge gates succeed.

After that merge, T252–T253 are authorized exactly once through:

`/run-v0.3-reference <exact-canonical-main-sha>`

The requested SHA must equal live canonical `main`. Baseline and eligible comparison skills execute before Diffcipline in the canonical order `baseline → karpathy → ponytail → diffcipline`. The run may not be selectively rerun because an arm or fixture loses, fails, times out, or produces no edit.

T254 begins only after the resulting artifact exists. It must validate:

- all 24 matrix rows are represented;
- every run bundle required by the workflow exists;
- base commits match across treatments for each fixture;
- runtime/model/treatment/sandbox identities match the pinned contract;
- exclusions, failures, and timeouts are explicit;
- reservation and provenance/checksum evidence are complete.

T255 may freeze the experiment only after T254 succeeds. Publication remains blocked until T255 is canonical.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, qualification requires private credentials, real execution cannot enforce containment, scoring becomes executor-specific or semantic, a dependency is proposed without demonstrated need, v0.1 evidence would need rewriting, the reference target has already been reserved/executed, or publication would hide failed/timed-out/excluded/losing evidence.
