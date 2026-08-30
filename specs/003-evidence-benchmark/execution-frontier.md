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

## Phase F entry and accepted execution

Containment implementation PR #51 exact head `82b701e43f3d64b57c9fc8da266cdc33489cdaf7` passed the reference, fixture, qualification, CI, and legacy regression workflows and merged as `f1f41f52a732230b39ac8cba082db262a0d58c9e`.

Pinned execution-body PR #52 exact head `b089c4b06c41aa62848bf8a5ae9f5eb420f5d0f3` passed `benchmark-v0.3-reference` `33264366591`, `benchmark-v0.3-qualification` `33264366617`, `benchmark-fixtures` `33264366590`, and `ci` `33264366589`, then merged as canonical `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea`. Exact post-merge `benchmark-fixtures` `33264509821`, `benchmark-v0.3-qualification` `33264509832`, and `ci` `33264510009` were SUCCESS. Qualification artifact `9718225574`, digest `sha256:2d9c782799b376b6c61ccb617941e4f7dbc6d93a1d7efa757c9d3794f2b2bd94`, proved containment and the 24-row matched contract without comparative model execution.

T250–T251 became canonical at `234f007dc8765f7b7649ada7d7d1d00ae4c12538`.

The one authorized comparative execution then ran exactly once as `benchmark-v0.3-reference` `33269484561` (#16) against that exact canonical target after qualification run `33269349342`. The run completed `SUCCESS`, produced reservation artifact `9719653684` with digest `sha256:f63e381cb199a064b875cdaf25eba614f3ea9b38048cd20bfbc18a689d6e28b7`, and produced raw results artifact `9720290597` with digest `sha256:dcad221a52e110a34198109ac31bfe164e2ac47610e78b83b9d98f17102c3218`.

The accepted `attempt-001` contains 24 rows in canonical treatment order: 12 `included`, 12 `failed`, 0 `timed_out`, and 0 `excluded`. All required run bundles are present; fixture base commits and comparison-contract digests match across treatments; runtime/model/treatment/sandbox provenance matches the pinned contract; and no failed or losing result was selectively rerun.

T254 independently downloaded artifact `9720290597`; its bytes matched the GitHub-recorded SHA-256 exactly. The attempt-local pre-packaging checksum ledger has 463 entries. The packaged artifact contains 295 of those referenced paths and all 295 match; 168 omitted entries are hidden `.git` metadata from duplicate ephemeral `work/` repositories. No required evidence bundle content is absent.

The frozen scorer remains unchanged. Test execution generated `__pycache__` files that the scorer counted as changed/unrelated/protected paths. Every treatment is `1/6` task-correct but `0/6` scorer-pass, all textual patches are empty, and no source-text edit was observed. This limitation is part of the accepted evidence and cannot justify a selective rerun or post-hoc scorer rewrite.

## Current benchmark truth

The accepted experiment does not establish a correctness advantage for Diffcipline or either comparison skill. Diffcipline had the largest summed task duration in the accepted run. Nine failed rows ended in provider/tool-parser HTTP 500 errors and three in internal agent request timeouts. Tokens and monetary cost are unavailable.

Publication records under `benchmarks/results/v0.3/` preserve the accepted run/artifact identity, digest, exact provenance, all observed treatment metrics, failure counts, checksum/package limitation, scorer limitation, unavailable metrics, and finite Actions-artifact retention boundary.

Raw artifact `9720290597` is the unfiltered publication surface emitted by the canonical workflow. Its GitHub retention expiry is `2026-11-27T18:54:06Z`; that finite retention is disclosed rather than represented as permanent storage.

## Immediate frontier

T252–T255 are complete by accepted evidence. T260–T262 are implemented on the current publication candidate.

The only authorized next task is **T263**: obtain machine-observed SUCCESS for repository CI, `benchmark-v0.3-qualification`, `skills-compat`, and `release` on the exact final publication head. Do not compose T264/T265 evidence from earlier heads.

After T263 succeeds:

1. reconcile submitted reviews, inline threads, and valid top-level findings;
2. verify canonical `main` has not moved unexpectedly;
3. merge only with the exact expected PR head;
4. verify exact post-merge gates on the resulting canonical `main` for T264;
5. author T265 as a separate completion record only after T264 is machine-observed;
6. claim `COMPLETE_CANONICAL` only after that completion record itself becomes canonical and its own post-merge state is verified.

No v0.3 release tag and no v1.0 implementation are authorized by this Spec 003 candidate.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, qualification requires private credentials, publication would hide failed/timed-out/excluded/losing evidence, the accepted artifact identity cannot be verified, or a proposed change would rewrite the frozen scorer/result boundary after observing the experiment.
