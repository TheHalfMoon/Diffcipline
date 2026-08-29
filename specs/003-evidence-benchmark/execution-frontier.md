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

Phase B T210–T215 became canonical at `5726c54f1b807a8d0976d71308c61cf70687d621` after PR #44 exact-head gates and these push runs succeeded on that exact commit:

- `benchmark-fixtures` `33257309999`: SUCCESS;
- `ci` `33257309939`: SUCCESS;
- `skills-compat` `33257309945`: SUCCESS;
- `release` `33257309947`: SUCCESS.

## Current benchmark truth

The repository contains a frozen six-task corpus, objective scorer, pinned v0.1 experiment, repository-local OpenAI-compatible agent loop, and a versioned v0.3 executor/treatment configuration. The remaining Phase C gap is a process-level adapter boundary so arm orchestration no longer selects `local_agent.py` directly.

## Immediate frontier

Phase C implements T220–T225 only:

- route `run_arm.py` through `executor_adapter.py`;
- keep the existing local OpenAI-compatible loop as the reference adapter;
- add a deterministic `contract-test` adapter used only for qualification;
- reject `contract-test` from comparative arm orchestration;
- preserve process exit, stdout, stderr, timeout state, transcript, treatment digest, adapter digest, and local-agent digest evidence;
- add standard-library contract and failure-path tests, including workspace-escape rejection.

T230 matrix work remains blocked until T220–T225 are canonical with exact-head and post-merge evidence.

The legacy `benchmark-arms` workflow may run after a canonical `run_arm.py` change. Any such run is legacy regression evidence only and cannot satisfy v0.3 T250–T255 or alter the frozen v0.1 canonical result.

## Real-experiment authorization boundary

No real comparative v0.3 experiment is authorized before T245. Contract fixtures/stubs may exercise the harness in CI, but their outputs must never be represented as model-comparison evidence.

After T245, execute only the exact pinned reference experiment defined by T250–T251. Do not selectively rerun losing tasks, drop failures, or change task/scorer inputs after observing results.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, executor/treatment identity cannot be separated, qualification requires private credentials, scoring becomes executor-specific or semantic, a dependency is proposed without demonstrated need, v0.1 evidence would need rewriting, comparative v0.3 execution is requested before T245, or publication would hide failed/timed-out/excluded/losing evidence.
