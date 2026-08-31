# Spec 004 — Universal Engineering Governor

## Status

`IMPLEMENTATION`

Planning authority became canonical at `df9c0216723d3e241b6cea99bfe58c6212c1cd6a` after exact-head and post-merge repository, skills, and release gates succeeded. Implementation remains ordered by `tasks.md` and cannot skip canonical phase boundaries.

## Roadmap authority

The canonical README defines v1.0 as **Universal engineering governor** with four goals:

1. stable proof schema;
2. broad agent portability;
3. signed release artifacts;
4. enterprise policy mode.

This specification turns those goals into a narrow deterministic contract. It builds on the completed v0.1–v0.3 system instead of replacing it.

## Product contract

### Stable proof schema

`diffcipline check --json` must emit a versioned v1 proof document with deterministic field ordering and explicit schema identity. The v1 schema must preserve the existing verdict, diff, scope, risk, reason, and verification evidence while adding enough policy provenance for layered enterprise enforcement.

A machine-readable schema artifact must be repository-versioned and tested against CLI output. Within schema major version 1, existing required fields and meanings cannot be removed or silently reinterpreted. Additive optional fields require tests and documentation.

### Enterprise policy mode

A repository may optionally supply an explicit enterprise baseline in addition to `.diffcipline.toml`. Enterprise enforcement is local-file only: Diffcipline does not fetch policy from a network service or require credentials.

Layering must be monotonic. A repository policy may tighten an enterprise baseline but must never weaken it. At minimum:

- file and line limits use the stricter bound;
- allow/review/fail decisions use the stricter decision;
- forbidden surfaces are cumulative;
- every non-empty expected-file contract remains independently enforceable;
- required verification commands are cumulative and deterministic;
- unsupported or malformed layered policy fails closed.

Proof output must disclose whether enterprise mode was active and which policy sources were evaluated.

### Broad agent portability

The Agent Skills core remains platform-neutral. Canonical compatibility must cover the existing six qualified clients—Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI—and a documented generic Agent Skills layout without creating platform-specific forks of the skill behavior.

Portability evidence must verify exact-head installation/discovery and the shared skill contract. Agent-specific wrappers may exist only when they are thin adapters; the canonical skill text remains the behavioral authority.

### Signed release artifacts

Every trusted canonical release-candidate path must build host-native binaries from locked Cargo inputs, create a deterministic SHA-256 manifest, produce GitHub/Sigstore provenance without repository-stored long-lived signing keys, and verify the attested binary subjects before the candidate is accepted.

This milestone does not itself authorize creating or moving a public version tag. Tag/public-release authority remains a separate irreversible boundary.

## Compatibility and preservation

- Preserve PASS / REVIEW / FAIL exit semantics: 0 / 1 / 2; usage/execution error remains 64.
- Preserve existing default `.diffcipline.toml` version 1 behavior when enterprise mode is not requested.
- Preserve v0.1, v0.2, and v0.3 canonical evidence and release history.
- Keep the Rust CLI runtime dependency-free unless a separately reviewed change proves a necessary net benefit.
- Preserve the portable Agent Skills core and existing GitHub Action behavior unless an explicit v1 contract change is specified.

## Non-goals

- remote policy control planes, SaaS administration, telemetry, or credential distribution;
- semantic or LLM-as-judge proof decisions;
- organization/user identity management, RBAC, billing, or hosted dashboards;
- silently auto-detecting an enterprise policy from outside the repository command invocation;
- rewriting accepted benchmark evidence or rerunning the v0.3 experiment;
- creating a v1.0 tag merely because the roadmap milestone is named v1.0.

## Qualification

Each implementation unit requires exact-head repository CI. Proof-schema changes additionally require schema contract tests; enterprise-policy changes require fail-closed and non-weakening tests; portability changes require skills compatibility; release changes require the release-candidate workflow.

Final completion requires one exact candidate head to pass `ci`, `skills-compat`, and `release`, plus any dedicated v1 qualification workflow introduced by this spec, followed by expected-head merge, exact post-merge verification, and a separate terminal completion record.

## Completion rule

Spec 004 is `COMPLETE_CANONICAL` only when all tasks are complete, the four roadmap capabilities are canonical, required exact-head and post-merge gates succeed, signed release-candidate provenance is machine-observed on canonical `main`, and the terminal completion record itself becomes canonical.
