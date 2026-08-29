# Current specification

Active: [`002-intent-aware-scope`](002-intent-aware-scope/spec.md)

Status: `ACTIVE_IMPLEMENTATION`

## Canonical read order

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. this file
4. `specs/002-intent-aware-scope/spec.md`
5. `specs/002-intent-aware-scope/plan.md`
6. `specs/002-intent-aware-scope/tasks.md`
7. `specs/002-intent-aware-scope/execution-frontier.md`
8. `.diffcipline.toml`
9. `crates/diffcipline-cli/src/main.rs`
10. `crates/diffcipline-cli/tests/cli.rs`
11. `action.yml`
12. `.github/workflows/ci.yml`

Live GitHub/repository truth overrides every recorded SHA below.

## Completed Spec 001 / v0.1

Spec 001 reached `COMPLETE_CANONICAL` on canonical `main` at `d74ed5f8789fb255e24f124e3283939cdc080cd0`.

The fixed `v0.1.0` tag remains directly at `ab434ae114b5f11ea9eb882bf572831dc7634531`. Release ID `378936458` is immutable. The v0.1 benchmark remains intentionally unfavorable and unchanged: all four arms scored `1/6`, all changed zero files, Diffcipline was slowest by observed wall-clock time, and no correctness advantage is supported.

## Spec 002 authority

The canonical README roadmap defines v0.2 as `Intent-aware scope` with exactly three product goals: expected/forbidden scope proof, risk-aware verification profiles, and GitHub PR annotation. Spec 002 narrows those goals deterministically and dependency-free.

T103 planning authority is canonical at `43aaf35c7a6b07b632e4707999cc664089f911ac`.

## Completed Phase B

T110–T115 expected/forbidden scope implementation is canonical at `b35ae01f7a83964ed1c5ab2431f8cf00f4fe3779` with exact post-merge `ci` `33250973190` and `release` `33250973214` successful.

## Completed Phase C

T120–T125 risk-aware verification implementation is canonical at `ef6b66a94029c102d5c798fdc8e71c68eeab61be` with exact post-merge `ci` `33251565005` and `release` `33251564986` successful.

## Completed Phase D

T130–T132 proof-output implementation is canonical at:

`fb231e21bc8e6ff0435e4056b196057ffc39d042`

Exact candidate evidence:

- PR #38 head `73de8af1ae368432d0ccfb29c7db31a354bd99cd`;
- `ci` `33254922245`: SUCCESS;
- `release` `33254922255`: SUCCESS;
- no submitted reviews or review threads and no valid automated finding.

Post-merge evidence:

- `ci` `33254995550`: SUCCESS;
- `release` `33254995552`: SUCCESS.

The proof contract now exposes selected/default risk, expected and forbidden intent contracts, deterministic scope violations, and per-command verification state while preserving existing human and JSON fields.

## Active frontier

T140–T144 are the next eligible unit: add an optional strictly validated GitHub Action `risk` input, forward it to the same CLI proof contract, preserve CLI exit semantics while capturing deterministic proof output, write a concise Markdown proof to `$GITHUB_STEP_SUMMARY` without write permissions or PR comments, and dogfood the annotation path in CI.

Do not begin v0.2 canonical closeout until T140–T144 are canonical with successful exact post-merge gates.
