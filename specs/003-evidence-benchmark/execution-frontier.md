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

Phase E T244 guarded reference entry and the T245 merge boundary merged at `3be4df7e19b7fd4410bb1127fdd91da9d2f27fc8`. PR #49 exact head `e1722417ec64200c0d218c1ba3a84d33c9fd247d` passed:

- `benchmark-v0.3-reference` `33262020518`: SUCCESS;
- `benchmark-v0.3-qualification` `33262020492`: SUCCESS;
- `benchmark-fixtures` `33262020534`: SUCCESS;
- `ci` `33262020505`: SUCCESS.

Exact post-merge canonical push evidence on `3be4df7e19b7fd4410bb1127fdd91da9d2f27fc8` is:

- `benchmark-v0.3-qualification` `33262094960`: SUCCESS;
- `benchmark-fixtures` `33262095055`: SUCCESS;
- `ci` `33262094948`: SUCCESS.

The post-merge qualification artifact is `9717538620`, digest `sha256:c8a5ccc984d86d58f18fc495c1d485b42434f4e51f12b8a03dde305655616a8d`, expires `2026-11-27T16:07:21Z`, and records:

- repository revision `3be4df7e19b7fd4410bb1127fdd91da9d2f27fc8`;
- result `PASS`;
- 24 matrix rows;
- `private_credentials_required=false`;
- `comparative_model_execution=false`;
- frozen v0.1 blobs unchanged.

`benchmark-v0.3-reference` intentionally has no push trigger. Its exact-head PR validation is the T244 proof; no comparative run was triggered by merge.

## Current benchmark truth

The public harness now has a canonical secret-free qualification path, deterministic executor/treatment/fixture orchestration, complete attempt-aware evidence contracts, a canonical order of `baseline → comparison skills sorted by id → diffcipline`, and a guarded owner-command real-experiment entry.

The current v0.3 experiment configuration already names the intended secret-free local reference lineage, but Phase F must independently freeze and verify the exact runtime/model/treatment provenance and real execution containment before any comparative arm is allowed to run.

## Immediate frontier

Phase F begins with T250–T251 only:

- freeze the exact local executor/runtime/model identity and every treatment revision/digest;
- verify every arm shares the same fixture revision, executor, model, prompt suffix, permissions, timeout, CPU, memory, and storage limits;
- enforce the declared `network_tools=denied`, `git_push=denied`, and `workspace=disposable-only` contract at real execution time, not only in JSON;
- extend the guarded reference workflow with a fully pinned execution body while keeping it inaccessible until T250/T251 are canonical;
- preserve canonical execution order `baseline → karpathy → ponytail → diffcipline`.

T252/T253 comparative execution remains blocked until T250/T251 and the execution body are canonical with exact-head and post-merge gates.

## Real-experiment authorization boundary

After T250/T251 become canonical, the only authorized real-experiment entry is an owner comment matching:

`/run-v0.3-reference <exact-canonical-main-sha>`

The workflow must verify the requested SHA equals live `main`, require exact successful qualification evidence for that SHA, enforce containment, run the exact pinned reference experiment once in canonical arm order, and preserve every failed/timed-out/excluded/losing artifact.

Do not selectively rerun losing tasks, drop failures, change task/scorer inputs after observing results, or substitute legacy v0.1 regression runs for v0.3 evidence.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, executor/treatment identity cannot be separated, qualification requires private credentials, real execution cannot enforce the declared containment contract, scoring becomes executor-specific or semantic, a dependency is proposed without demonstrated need, v0.1 evidence would need rewriting, comparative execution is requested before T250/T251 become canonical, or publication would hide failed/timed-out/excluded/losing evidence.
