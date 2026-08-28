# Specification 001 — Proof Before Done

## Problem

Coding agents can produce plausible changes while silently assuming requirements, touching unrelated files, over-building solutions, and declaring completion without enough evidence.

## Product statement

Diffcipline is a portable engineering-discipline skill plus a deterministic CLI that makes a coding agent reduce accidental complexity and prove the exact change before declaring success.

## User stories

### US1 — Developer using a coding agent

As a developer, I want my coding agent to prefer the smallest correct solution and avoid unrelated edits so that generated changes remain reviewable.

Acceptance:
- the skill explicitly requires understanding, need challenge, scope minimization, risk classification, and proof;
- safety and correctness cannot be removed for minimality.

### US2 — Developer reviewing a change

As a developer, I want one command to summarize the exact diff and verification state so I can distinguish evidence from agent narrative.

Acceptance:
- `diffcipline check` reads Git facts;
- output contains PASS, REVIEW, or FAIL;
- configured checks that were not executed are shown as NOT RUN and prevent PASS;
- hard policy violations produce FAIL.

### US3 — Team maintaining policy

As a team, I want repository-native policy for diff size, dependency churn, lockfiles, untracked files, and verification commands.

Acceptance:
- `.diffcipline.toml` is readable and versioned;
- unsupported policy keys fail closed rather than being silently ignored;
- verification command execution requires explicit `--run`.

## Non-goals for v0.1

- autonomous code generation;
- semantic AI judging in the CLI;
- cloud accounts or telemetry;
- a dashboard;
- a private model;
- opaque quality scores;
- broad platform adapters before the core contract is stable.

## Success criteria

v0.1 is releasable only when:
1. the Rust workspace formats, lints, and tests cleanly;
2. proof verdict behavior is covered by tests;
3. policy parsing fails on unknown fields;
4. a fixture repository demonstrates PASS, REVIEW, and FAIL cases;
5. installation and security docs describe verification-command trust boundaries;
6. the benchmark protocol is public before any performance claim appears in README.
