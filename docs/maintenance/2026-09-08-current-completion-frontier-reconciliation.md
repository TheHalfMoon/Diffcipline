# Current completion frontier reconciliation

Date: 2026-09-08

## Authorization

This is a separately authorized post-completion maintenance unit under Issue #98.

The maintainer authorized continuing until the project is genuinely finished and granted ordinary approval for evidence-backed maintenance work. This unit does not reopen, extend, or replace Specs 001–008.

## Starting canonical truth

Canonical `main` at maintenance start:

`4349c54c96eb7ab2041eef2249ad058260e0a648`

At that commit:

- Specs 001–008 were already `COMPLETE_CANONICAL`;
- there was no active implementation specification;
- there were no open pull requests;
- there were no open issues before Issue #98 was created;
- public `v1.0.0` remained immutable;
- live repository metadata had already been reconciled.

## Observed contradiction

`specs/CURRENT.md` correctly declared `COMPLETE_CANONICAL` and no active specification, but still contained candidate-era language that was no longer true after PR #93 had merged and its post-merge qualification had completed.

Examples included:

- `Until those conditions are machine-observed`;
- `Branch docs/008-complete-canonical is the sole remaining Spec 008 unit`;
- completion language written as a future condition even though T843 was already canonical.

Because `specs/CURRENT.md` is the repository's current-state authority surface, that stale frontier language was a real governance contradiction rather than a cosmetic preference.

## Authorized scope

- reconcile `specs/CURRENT.md` into an unambiguous post-completion current-state record;
- preserve exact historical completion evidence and limitations;
- add this maintenance record;
- close Issue #98 only after exact post-merge qualification and final frontier verification.

## Explicitly out of scope

- runtime, CLI, Agent Skill, GitHub Action, schema, policy, or workflow behavior changes;
- dependencies, manifests, or lockfiles;
- benchmark execution, rescoring, or comparative claims;
- release, tag, asset, or provenance mutation;
- reopening or extending Specs 001–008;
- changing historical `docs/DISCOVERABILITY.md`;
- new adoption, popularity, endorsement, or superiority claims;
- manufacturing a successor specification or feature roadmap.

## Preserved canonical evidence

Spec 008 completion record PR #93 exact head:

`ca726dae9a6f4e28dd8653f5c8c9da22c460be2a`

PR #93 merged to:

`3bb0fdaf7c6d7a77fa586dd320acf4a0d0b5e2d9`

Exact post-merge workflows on that canonical commit completed `SUCCESS`:

- `ci` `33485424611`;
- `skills-compat` `33485424488`;
- `release` `33485424445`.

This maintenance unit does not reinterpret or strengthen those claims; it only removes stale future-tense frontier language from the current-state surface.

## Workflow qualification

GitHub's actual workflow selection is authoritative for both the pull-request event and the resulting canonical push.

Every workflow GitHub selects for the exact PR head must complete `SUCCESS` before merge. Queued, in-progress, missing, stale, filtered-out, or unavailable runs are not PASS.

Before merge, reviews, review threads, comments, mergeability, exact head, and canonical `main` must be reconciled. Merge must use the expected-head guard and must not rewrite shared history.

After merge, every workflow GitHub selects for the exact canonical push must complete `SUCCESS` before this maintenance unit is considered complete.

## Completion rule

This unit is complete only when:

1. the exact PR head passes every workflow GitHub selects;
2. review/thread/comment/mergeability/head/main reconciliation is clean;
3. the PR merges by expected head without history rewriting;
4. every workflow selected for the resulting canonical push completes `SUCCESS`;
5. `specs/CURRENT.md` on canonical `main` contains no stale remaining-frontier claim;
6. historical `docs/DISCOVERABILITY.md` still has blob `013791e04fd30607f1f64f4a8218c000a8f0ab73`;
7. public `v1.0.0` remains immutable;
8. Issue #98 is closed only after the above evidence exists;
9. the repository returns to no open PR or issue frontier unless independent new work arrives.

Until all conditions are machine-observed, canonical `main` remains authoritative and this branch is only a maintenance candidate.
