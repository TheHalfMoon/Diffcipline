# Live GitHub metadata truth reconciliation

Date: 2026-09-08

## Authorization

This is a separately authorized maintenance unit following canonical completion of Specs 001–008. The maintainer authorized continuing until the project is genuinely finished and granted ordinary authorization to complete remaining evidence-backed project work.

This unit does not reopen, extend, or replace any completed specification.

## Observed contradiction

At canonical `main` `60276fd8c74f88a23c7f256c97dcba9fdf50018c`, repository-controlled current-status documentation still preserved the earlier metadata state `NOT APPLIED — TOOLING UNAVAILABLE`.

The authenticated live GitHub repository API instead reported:

- description: `Proof-before-done verification for coding agents through Agent Skills, a dependency-free Rust CLI, and a pinned GitHub Action.`;
- topics: `agent-skills`, `ai-agents`, `code-quality`, `coding-agents`, `developer-tools`, `github-actions`, `rust`, `verification`;
- homepage: unset.

Repository truth therefore required a bounded documentation reconciliation.

## Authorized scope

- update `specs/CURRENT.md` so its current metadata statement matches live GitHub truth;
- update `docs/GITHUB-METADATA.md` while preserving the historical Phase C observation and recording the later live reconciliation;
- record this maintenance unit;
- close Issue #96 after canonical post-merge verification succeeds.

## Explicitly out of scope

- runtime, CLI, Agent Skill, GitHub Action, schema, policy, or workflow behavior changes;
- dependency, manifest, or lockfile changes;
- benchmark execution, rescoring, or comparative claims;
- release, tag, asset, or provenance changes;
- reopening or extending Specs 001–008;
- changing frozen `docs/DISCOVERABILITY.md`;
- new adoption, popularity, endorsement, or superiority claims;
- homepage creation or any further repository metadata mutation.

## Preserved history

The Phase C observation that metadata was `NOT APPLIED — TOOLING UNAVAILABLE` remains valid for that historical point in time. This unit does not rewrite that observation; it distinguishes it from the current live state.

Historical `docs/DISCOVERABILITY.md` remains untouched and must retain blob `013791e04fd30607f1f64f4a8218c000a8f0ab73`.

Public `v1.0.0` remains immutable and unchanged.

## Workflow applicability

GitHub's exact PR-head selection is authoritative. Because this unit changes `specs/CURRENT.md`, the observed PR event selected all nine repository qualification workflows:

- `ci`;
- `skills-compat`;
- `release`;
- `stage-v0.1.0-release`;
- `tag-v0.1.0`;
- `verify-v0.1.0-release`;
- `stage-v1.0.0-release`;
- `tag-v1.0.0`;
- `verify-v1.0.0-release`.

Each selected workflow must be evaluated only on the exact PR head and, after merge, every workflow selected by GitHub on the exact resulting canonical commit must also succeed. A queued, in-progress, missing, skipped, stale, or different-head run is not a PASS.

## Completion rule

This unit is complete only when:

1. the exact PR head passes all nine observed qualification workflows listed above;
2. reviews, review threads, comments, mergeability, exact head, and canonical `main` are reconciled;
3. the PR merges by expected head without rewriting shared history;
4. every workflow selected by GitHub for the resulting canonical push succeeds on that exact canonical commit;
5. live GitHub metadata is re-verified after the merge;
6. `docs/DISCOVERABILITY.md` still has blob `013791e04fd30607f1f64f4a8218c000a8f0ab73`;
7. Issue #96 is closed only after the above evidence exists.

Until all conditions are machine-observed, this reconciliation remains a candidate and canonical `main` remains authoritative.
