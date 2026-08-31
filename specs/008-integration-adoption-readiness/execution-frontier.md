# Execution Frontier — Spec 008

Live GitHub/repository truth overrides this snapshot.

## Canonical prerequisite

Spec 007 closeout: `108ed30e9d8fd00b7d0a6202cba5c433476c9ea9`.

Public `v1.0.0` remains immutable at `5cb1c77340b75649f6168e0e8f66479ea047ea96`.

## Canonical activation

Planning PR #88 exact head `693e1bc81af394e77c96e7a373be8118ca301bb3` passed all nine required pull-request workflows and reconciled cleanly before expected-head squash merge.

Canonical activation: `60fb2643c2710f0e262c2b007ca4192f039d30c3`.

Exact post-merge:

- `ci` `33439088987` — `SUCCESS`;
- `skills-compat` `33439088957` — `SUCCESS`;
- `release` `33439088976` — `SUCCESS`.

## Canonical Phase B

PR #89 exact head `015c0196b646d7eafd231de6607e57d5d633f23a` passed all nine required workflows after the preserved initial rustfmt failure was corrected on a new exact head. Reconciliation found no submitted reviews or inline threads, only non-substantive automated comments, and unchanged canonical `main` before expected-head merge.

Canonical Phase B: `b31d891427b5ddbd43fc24c2ad2e1dc7adc6bd39`.

Exact post-merge:

- `ci` `33440059674` — `SUCCESS`;
- `skills-compat` `33440059726` — `SUCCESS`;
- `release` `33440059755` — `SUCCESS`.

The checked-in Rust, Node, Python, and Go policies are therefore canonical. Their integration test loads the exact files and requires proof-v1 repository provenance, `REVIEW` without verification execution, and documented commands reported as `NOT RUN`.

## Phase C candidate

Branch: `docs/008-adoption-independent-validation`.

The candidate adds:

1. `docs/ADOPTION.md` — one bounded adoption path across canonical Agent Skills, CLI/policy examples, risk profiles, and the immutable GitHub Action;
2. `docs/INDEPENDENT-VALIDATION.md` — a reproducible protocol against fixed `v1.0.0` covering source identity, release/asset/attestation verification, CLI proof semantics, Agent Skills identity, retained evidence, and explicit `NOT RUN` / `NOT AVAILABLE` states;
3. human and machine-readable links from `README.md` and `llms.txt`.

The independent-validation document is a protocol only. It records no external execution, endorsement, adoption result, or benchmark treatment effect.

## Current limitations carried forward

- repository description is unset;
- topics are empty;
- homepage is unset;
- broad public discovery/adoption remains weak in the bounded Spec 007 audit;
- unavailable independent model recommendation surfaces remain untested;
- the authenticated execution surface has not yet exposed a repository-metadata mutation action.

## Next gate

T823 requires exact-head qualification of this Phase C candidate, clean review/thread/comment and canonical-main reconciliation, expected-head merge, and exact post-merge `ci`, `skills-compat`, and `release` success before Phase D begins.
