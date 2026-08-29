# Current specification

Active: [`002-intent-aware-scope`](002-intent-aware-scope/spec.md)

Status: `COMPLETE_CANONICAL`

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

The canonical README roadmap defines v0.2 as `Intent-aware scope` with exactly three product goals: expected/forbidden scope proof, risk-aware verification profiles, and GitHub job-summary annotation. Spec 002 implements those goals deterministically and dependency-free.

T103 planning authority is canonical at `43aaf35c7a6b07b632e4707999cc664089f911ac`.

## Completed Phase B

T110–T115 expected/forbidden scope implementation is canonical at `b35ae01f7a83964ed1c5ab2431f8cf00f4fe3779` with exact post-merge `ci` `33250973190` and `release` `33250973214` successful.

## Completed Phase C

T120–T125 risk-aware verification implementation is canonical at `ef6b66a94029c102d5c798fdc8e71c68eeab61be` with exact post-merge `ci` `33251565005` and `release` `33251564986` successful.

## Completed Phase D

T130–T132 proof-output implementation is canonical at `fb231e21bc8e6ff0435e4056b196057ffc39d042` with exact post-merge `ci` `33254995550` and `release` `33254995552` successful.

The proof contract exposes selected/default risk, expected and forbidden intent contracts, deterministic scope violations, and per-command verification state while preserving existing human and JSON fields.

## Completed Phase E

T140–T144 GitHub Action annotation is canonical at `c059fc76e4d836e7f9e10ce4bb0465428791ed40` after PR #40 exact head `ec87a121ddf1958f9b57f300699da0457e219b43` passed `ci` `33255469452`, followed by successful post-merge `ci` `33255652466`.

The Action accepts an optional strictly validated risk input, forwards it to the same CLI contract, preserves the CLI exit status while capturing proof, writes the deterministic proof section to `$GITHUB_STEP_SUMMARY`, and requires no repository write permission or PR comment.

## Completed Phase F

PR #41 exact head:

`6e10466fb28687aba48ca363135dbff5253bd1db`

Exact-head closeout evidence:

- `ci` `33255846426`: SUCCESS;
- `skills-compat` `33255846412`: SUCCESS;
- `release` `33255846514`: SUCCESS;
- `tag-v0.1.0` validation `33255846439`: SUCCESS;
- `stage-v0.1.0-release` validation `33255846449`: SUCCESS;
- `verify-v0.1.0-release` validation `33255846466`: SUCCESS;
- no submitted reviews or review threads remained; top-level automated comments contained no code finding;
- canonical `main` remained at the exact candidate base until merge.

PR #41 was squash-merged as:

`246cac79d8c1a2774b8fa7aad60ccb9efb4b40cd`

with tree:

`ca9bfabdb3e4ebccae2781862237344e2a9f1531`

Exact post-merge evidence:

- `ci` `33255959784`: SUCCESS;
- `skills-compat` `33255959806`: SUCCESS;
- `release` `33255959768`: SUCCESS.

T153 was machine-observed before this completion record was authored. T150–T154 are recorded complete in the Spec 002 task ledger.

## Completion state

Spec 002 / v0.2 is recorded as `COMPLETE_CANONICAL` by this evidence change. This status is not an external completion claim until this exact evidence change is itself merged to canonical `main` and the resulting post-merge state is verified.

No `v0.2.0` tag was created or authorized. Any v0.3 work requires its own canonical authority chain rather than extending Spec 002 implicitly.
