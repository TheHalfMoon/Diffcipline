# Spec 004 — Universal Engineering Governor

## Status

`COMPLETE_CANONICAL`

This status is effective only after this terminal completion record is merged to canonical `main` and the required exact post-merge gates succeed on that resulting canonical SHA. Before those conditions hold, this branch is only the terminal completion candidate.

Planning authority became canonical at `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`. The stable proof schema, enterprise policy mode, broad agent portability, signed release-candidate contract, and integrated capability milestone subsequently became canonical in the ordered phases defined by `tasks.md`.

## Roadmap authority

The canonical README defines v1.0 as **Universal engineering governor** with four goals:

1. stable proof schema;
2. broad agent portability;
3. signed release artifacts;
4. enterprise policy mode.

This specification turns those goals into a narrow deterministic contract. It builds on the completed v0.1–v0.3 system instead of replacing it.

## Product contract

### Stable proof schema

`diffcipline check --json` emits a versioned v1 proof document with deterministic field ordering and explicit schema identity. The v1 schema preserves the existing verdict, diff, scope, risk, reason, and verification evidence while including policy provenance for layered enterprise enforcement.

The repository-versioned schema artifact is tested against CLI output. Within schema major version 1, existing required fields and meanings cannot be removed or silently reinterpreted. Additive optional fields require tests and documentation.

### Enterprise policy mode

A repository may optionally supply an explicit enterprise baseline in addition to `.diffcipline.toml`. Enterprise enforcement is local-file only: Diffcipline does not fetch policy from a network service or require credentials.

Layering is monotonic. A repository policy may tighten an enterprise baseline but must never weaken it. At minimum:

- file and line limits use the stricter bound;
- allow/review/fail decisions use the stricter decision;
- forbidden surfaces are cumulative;
- every non-empty expected-file contract remains independently enforceable;
- required verification commands are cumulative and deterministic;
- unsupported or malformed layered policy fails closed.

Proof output discloses whether enterprise mode was active and which policy sources were evaluated.

### Broad agent portability

The Agent Skills core remains platform-neutral. Canonical compatibility covers Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Gemini CLI, and the documented generic Agent Skills layout without platform-specific forks of the skill behavior.

Portability evidence verifies exact-head installation/discovery and the shared skill contract. Agent-specific wrappers may exist only when they are thin adapters; the canonical skill text remains the behavioral authority.

### Signed release artifacts

Every trusted canonical release-candidate path builds host-native binaries from locked Cargo inputs, creates a deterministic SHA-256 manifest, produces GitHub/Sigstore provenance without repository-stored long-lived signing keys, and verifies the attested binary subjects before the candidate is accepted.

This specification does not authorize creating or moving a public v1 version tag. Tag/public-release authority remains a separate irreversible boundary.

## Compatibility and preservation

- Preserve PASS / REVIEW / FAIL exit semantics: 0 / 1 / 2; usage/execution error remains 64.
- Preserve existing default `.diffcipline.toml` version 1 behavior when enterprise mode is not requested.
- Preserve v0.1, v0.2, and v0.3 canonical evidence and release history.
- Keep the Rust CLI runtime dependency-free unless a separately reviewed change proves a necessary net benefit.
- Preserve the portable Agent Skills core and existing GitHub Action behavior unless a later canonical specification explicitly changes them.

## Non-goals

- remote policy control planes, SaaS administration, telemetry, or credential distribution;
- semantic or LLM-as-judge proof decisions;
- organization/user identity management, RBAC, billing, or hosted dashboards;
- silently auto-detecting an enterprise policy from outside the repository command invocation;
- rewriting accepted benchmark evidence or rerunning the v0.3 experiment;
- creating a v1.0 tag merely because the roadmap milestone is named v1.0.

## Qualification

Each implementation unit required exact-head repository CI. Proof-schema changes additionally required schema contract tests; enterprise-policy changes required fail-closed and non-weakening tests; portability changes required skills compatibility; release changes required the release-candidate workflow.

Final capability qualification used one exact candidate head for `ci`, `skills-compat`, and `release`, followed by expected-head merge and exact post-merge repository, portability, schema/policy, checksum, signed-provenance, and attestation-subject verification.

## Completion rule

Spec 004 is `COMPLETE_CANONICAL` only when all tasks are complete, the four roadmap capabilities are canonical, required exact-head and post-merge gates succeed, signed release-candidate provenance is machine-observed on canonical `main`, and this terminal completion record itself is canonical with successful required post-merge gates.
