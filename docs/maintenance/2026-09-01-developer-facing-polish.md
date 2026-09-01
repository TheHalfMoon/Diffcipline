# Developer-facing polish maintenance unit

Date: 2026-09-01

## Authorization

This is a separately authorized maintenance unit following canonical completion of Specs 001–008. The maintainer explicitly authorized making the repository more professional and attractive to developers.

This maintenance unit does not reopen, extend, or replace any completed specification.

## Intent

Improve the repository's first-run developer experience without changing Diffcipline's runtime behavior, proof semantics, benchmark record, release contents, or completed specification history.

## Authorized scope

- improve `README.md` information hierarchy, onboarding, navigation, and developer-facing presentation while preserving evidence-backed claims;
- add a pull request template that encodes existing contribution and proof expectations;
- record this bounded maintenance unit.

## Explicitly out of scope

- CLI or Agent Skill behavior changes;
- workflow or GitHub Action behavior changes;
- dependency, manifest, or lockfile changes;
- benchmark execution, rescoring, or historical evidence changes;
- release, tag, asset, or provenance changes;
- changes to completed Specs 001–008;
- new comparative, adoption, popularity, endorsement, or superiority claims;
- repository metadata mutation when the execution surface does not expose a supported mutation action.

## Completion rule

This maintenance unit is complete only when its exact pull-request head passes the repository's required pull-request qualification, review/thread/comment/mergeability/main reconciliation is clean, it merges by expected head, and the resulting canonical commit passes the required post-merge `ci`, `skills-compat`, and `release` workflows.

Until those conditions are machine-observed, the maintenance work remains a candidate and canonical `main` remains authoritative.
