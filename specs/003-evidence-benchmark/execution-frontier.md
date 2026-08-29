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

## Current benchmark truth

The repository now has:

- the frozen six-task corpus and objective scorer;
- the pinned historical v0.1 experiment and unfavorable canonical result;
- a versioned v0.3 executor/treatment configuration;
- a process-level executor adapter with the existing local OpenAI-compatible loop as reference adapter;
- a deterministic qualification-only `contract-test` adapter excluded from comparative evidence;
- deterministic executor × treatment × fixture expansion;
- matched comparison-contract digests;
- attempt-aware output directories that do not overwrite prior attempts;
- explicit manifest states for included, failed, timed-out, and excluded runs.

The next gap is reproducibility qualification and a guarded explicit real-experiment entry path.

## Immediate frontier

Phase E implements T240–T245 only:

- add secret-free harness qualification using deterministic fixtures/adapters;
- run config, adapter, matrix, matching, evidence-completeness, and scorer-boundary tests in CI;
- prove the canonical qualification path needs no private credentials;
- prove frozen v0.1 fixture/scorer/history remain unchanged;
- define an explicit real-experiment workflow that cannot execute on ordinary pull requests;
- merge and post-merge verify the qualified public harness before authorizing comparative execution.

CI qualification may use deterministic contract fixtures and adapters. Those outputs are qualification evidence only, never model-comparison evidence.

## Real-experiment authorization boundary

No real comparative v0.3 experiment is authorized before T245 becomes canonical.

After T245, execute only the exact pinned reference experiment defined by T250–T251. Baseline and eligible comparison skills must run before the Diffcipline arm under the same executor/model/task/revision/permissions/prompt/timeout/resource contract. Do not selectively rerun losing tasks, drop failures, or change task/scorer inputs after observing results.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, executor/treatment identity cannot be separated, qualification requires private credentials, scoring becomes executor-specific or semantic, a dependency is proposed without demonstrated need, v0.1 evidence would need rewriting, comparative v0.3 execution is requested before T245, or publication would hide failed/timed-out/excluded/losing evidence.
