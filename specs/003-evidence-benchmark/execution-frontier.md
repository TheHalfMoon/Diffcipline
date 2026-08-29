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

## Planning authority evidence

T203 became canonical at `c392d372564b55cc7d55aee8bed1b2641dee6820` after PR #43 passed exact-head gates, merged to unchanged `main`, and the following push runs succeeded on that exact commit:

- `ci` `33256584608`: SUCCESS;
- `skills-compat` `33256584575`: SUCCESS;
- `release` `33256584593`: SUCCESS.

## Current benchmark truth

The repository already contains:

- a six-task deterministic fixture corpus;
- an objective repository-state scorer;
- a pinned v0.1 local model/runtime configuration;
- a repository-local OpenAI-compatible bash-tool agent loop;
- arm orchestration that currently hardcodes that local agent;
- raw v0.1 evidence and publication artifacts.

The v0.3 gap is the executor-independent public harness and reproducible multi-executor evidence contract, not a missing scorer.

## Immediate frontier

Phase B implements T210–T215 only:

- a new `benchmarks/v0.3/experiment.json` schema separate from frozen v0.1 `run-config.json`;
- executor profiles independent from treatment arms;
- fail-closed validation of IDs, adapter kinds, revisions/digests, and resource limits;
- explicit denied network/Git-push permissions and disposable workspace policy;
- deterministic normalized serialization;
- standard-library unit coverage for valid and invalid configurations.

T220 adapter work remains blocked until T210–T215 are canonical with exact-head and post-merge evidence.

## Real-experiment authorization boundary

No real comparative v0.3 experiment is authorized before T245. Contract fixtures/stubs may exercise the harness in CI, but their outputs must never be represented as model-comparison evidence.

After T245, execute only the exact pinned reference experiment defined by T250–T251. Do not selectively rerun losing tasks, drop failures, or change task/scorer inputs after observing results.

## Stop conditions

Stop rather than weaken governance if:

- canonical `main` changes unexpectedly during candidate evaluation;
- a required exact-head or post-merge workflow is missing or failing;
- a valid review finding remains unresolved;
- executor and treatment identity cannot be separated deterministically;
- a proposed canonical qualification requires private credentials;
- the scorer would need executor-specific or semantic/LLM judging;
- a dependency becomes necessary without demonstrated benefit;
- v0.1 frozen evidence would need rewriting;
- comparative execution is requested before T245;
- publication would require hiding failed, timed-out, excluded, or losing evidence.
