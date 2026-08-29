# Specification 002 — Intent-Aware Scope

## Problem

Diffcipline v0.1 can prove diff size, dependency churn, untracked state, and configured verification, but it does not know whether the changed files are the files the task intended to touch or whether a sensitive repository surface was explicitly out of bounds. It also applies one verification command set regardless of declared risk, and the GitHub Action reports only job success/failure rather than a compact PR-facing proof summary.

## Product statement

Diffcipline v0.2 adds deterministic intent-aware scope contracts, risk-aware verification profiles, and PR-facing proof annotations without introducing semantic AI judging or a runtime dependency.

## User stories

### US1 — Expected-file proof contract

As a maintainer, I want repository policy to declare expected changed-file patterns and forbidden surface patterns so that an agent cannot receive PASS after editing outside the intended scope.

Acceptance:
- policy supports optional `expected_files` and `forbidden_surfaces` arrays;
- matching is deterministic, repository-relative, and documented;
- a changed file outside every expected pattern produces FAIL when expected patterns are configured;
- a changed file matching any forbidden pattern produces FAIL;
- unknown intent keys fail closed;
- human and JSON proof output expose scope violations.

### US2 — Risk-aware verification profiles

As a maintainer, I want the check command to select verification commands by explicit risk level so higher-risk work can require stronger repository-native checks.

Acceptance:
- `check --risk <R0|R1|R2|R3>` is explicit and deterministic;
- policy supports verification profiles for R0–R3;
- an explicitly selected profile overrides the default command list;
- requesting a risk profile that is not configured fails closed rather than silently using weaker checks;
- omitting `--risk` preserves v0.1 default verification behavior.

### US3 — GitHub PR annotation

As a pull-request reviewer, I want the Diffcipline Action to publish a concise proof summary in the GitHub job summary so scope, risk, verdict, and verification state are visible without parsing raw logs.

Acceptance:
- the composite Action can accept an optional risk input;
- it runs the same CLI contract used locally;
- it emits Markdown to `$GITHUB_STEP_SUMMARY` from deterministic CLI JSON/human evidence;
- annotation does not require write permissions or comments;
- the action still exits according to the CLI PASS/REVIEW/FAIL contract.

## Matching contract

Intent patterns use a deliberately small dependency-free matcher:
- exact repository-relative path matches exactly;
- a suffix `/**` matches the named directory and all descendants;
- a leading `*.` matches a filename suffix in any directory;
- all other `*` placements are unsupported and fail policy parsing.

This is not a general glob engine. Narrow semantics are intentional for portability and auditability.

## Non-goals for v0.2

- semantic interpretation of task prose;
- inferred risk from source code;
- arbitrary glob syntax;
- GitHub API write access or automatic PR comments;
- changing the v0.1 benchmark result;
- adding a runtime dependency;
- stable v1 JSON schema guarantees.

## Success criteria

v0.2 is complete only when:
1. intent contract policy parsing fails closed on unsupported keys/patterns;
2. expected-file and forbidden-surface behavior has unit and fixture-repository regression coverage;
3. risk profile selection has unit and integration coverage including missing-profile failure;
4. existing v0.1 policy files remain valid and behavior-compatible when new fields are absent;
5. human and JSON output expose intent/risk evidence;
6. the GitHub Action writes a deterministic job summary and forwards optional risk;
7. exact-head Rust, dogfood, skills compatibility, and release-candidate workflows remain green;
8. canonical completion evidence is merged to `main` before `COMPLETE_CANONICAL` is claimed.
