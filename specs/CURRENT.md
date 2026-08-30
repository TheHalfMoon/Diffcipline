# Current specification

Active: none

Most recently completed: [`003-evidence-benchmark`](003-evidence-benchmark/spec.md)

Status: `COMPLETE_CANONICAL`

This terminal status becomes effective only when this completion record is itself merged to canonical `main` and its required post-merge gates are machine-observed successful. Before that merge, this branch is only the Spec 003 completion candidate.

## Canonical read order

When no specification is active, read:

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. `README.md` roadmap and benchmark doctrine
4. this file
5. the most recently completed specification authority chain
6. repository governance and workflows relevant to any proposed next planning change.

A later roadmap item does not silently become an active implementation specification. Any next specification must establish its own canonical authority before implementation.

Live GitHub/repository truth overrides every recorded SHA below.

## Completed Spec 001 / v0.1

Spec 001 reached `COMPLETE_CANONICAL` at `d74ed5f8789fb255e24f124e3283939cdc080cd0`. The fixed `v0.1.0` tag remains directly at `ab434ae114b5f11ea9eb882bf572831dc7634531`; Release ID `378936458` is immutable.

The canonical v0.1 benchmark remains intentionally unfavorable: baseline, Karpathy, Ponytail, and Diffcipline each scored `1/6`; all four arms changed zero files; Diffcipline was slowest; and no correctness advantage is supported. Invalid run `33195457215` remains excluded.

## Completed Spec 002 / v0.2

Spec 002 reached `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. Final post-merge `ci` `33256238377`, `skills-compat` `33256238390`, and `release` `33256238367` were SUCCESS. No `v0.2.0` tag was authorized or created.

## Spec 003 / v0.3 canonical history

The README defines v0.3 as **Evidence benchmark**: a public multi-agent benchmark harness with reproducible baselines against unassisted agents and other skills. Spec 003 preserves frozen v0.1 evidence and forbids semantic/LLM-as-judge scoring, selective reruns, hidden exclusions, v1.0 work under Spec 003, and a v0.3 release tag.

Planning T200–T203 became canonical at `c392d372564b55cc7d55aee8bed1b2641dee6820`. Phases B–E and the guarded Phase F implementation became canonical through `234f007dc8765f7b7649ada7d7d1d00ae4c12538`, which established the exact one-shot public reference-experiment boundary.

Canonical workflow run `33269484561` (#16) then executed exactly once against `234f007dc8765f7b7649ada7d7d1d00ae4c12538` after qualification run `33269349342`. It produced raw results artifact `9720290597`, digest `sha256:dcad221a52e110a34198109ac31bfe164e2ac47610e78b83b9d98f17102c3218`, plus reservation artifact `9719653684`, digest `sha256:f63e381cb199a064b875cdaf25eba614f3ea9b38048cd20bfbc18a689d6e28b7`.

The accepted experiment contains 24 rows: 12 `included`, 12 `failed`, 0 `timed_out`, and 0 `excluded`. Base commits, comparison contracts, runtime/model/treatment/sandbox provenance, qualification, and containment were validated. No failed or losing result was selectively rerun.

All treatments were `1/6` task-correct. The unchanged frozen scorer reported `0/6` scorer-pass for every treatment because fixture verification generated Python `__pycache__` files that the scorer counted as changed/unrelated/protected paths. All textual patches were empty. This limitation remains published rather than repaired post hoc. Nine failed rows ended in provider/tool-parser HTTP 500 errors and three in internal agent request timeouts. Tokens and monetary cost are unavailable.

Publication records under `benchmarks/results/v0.3/` preserve the accepted run/artifact identity, exact provenance, metrics, failures, packaging/checksum limitation, scorer limitation, unavailable metrics, and finite Actions-artifact retention boundary.

## Spec 003 terminal evidence

PR #54 final exact head `e5e3b2675af2af55426229dc4afbbb349db956d8` passed `benchmark-v0.3-qualification` `33301772574`, `skills-compat` `33301772570`, `release` `33301772566`, and `ci` `33301772564`, all `SUCCESS` on the same head. No submitted reviews or inline threads remained.

PR #54 was expected-head squash-merged as canonical `d59cc6ec570c894713d6bf32aa0b4af9d60d7c38`. Exact post-merge push `ci` `33301846572`, `benchmark-v0.3-qualification` `33301846507`, `skills-compat` `33301846603`, and `release` `33301846610` all completed `SUCCESS`. T264 was therefore machine-observed before this completion record was authored.

This completion record marks T265 and Spec 003 `COMPLETE_CANONICAL`. The claim is valid only once this record itself is canonical and its post-merge gates are successful.

## Next roadmap boundary

Spec 003 does not authorize v1.0 implementation and does not create a v0.3 release tag. After this completion record becomes canonical, re-read canonical `main`, the README roadmap, `AGENTS.md`, `CONSTITUTION.md`, and all repository governance before creating any next specification. Planning for a later roadmap item may proceed only if that canonical authority allows it; implementation requires the next specification to become canonical first.
