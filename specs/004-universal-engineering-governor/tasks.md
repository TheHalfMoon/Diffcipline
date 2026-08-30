# Tasks — 004 Universal Engineering Governor

## Phase A — Canonical planning

- [x] T400 Derive the v1 capability contract from the canonical README and completed v0.x truth.
- [x] T401 Define compatibility, preservation, non-goals, and irreversible release boundaries.
- [x] T402 Define ordered implementation and qualification phases.
- [x] T403 Merge Spec 004 planning authority to canonical `main` and verify exact post-merge gates.

T403 exact evidence:

- planning PR #56 exact head `cb590fde5dc3bf76abee1ec3bd8b512607d63dcf` passed `ci` `33302675371`, `skills-compat` `33302675367`, and `release` `33302675373`;
- expected-head squash merge produced canonical `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`;
- exact post-merge `ci` `33302752212`, `skills-compat` `33302752218`, and `release` `33302752209` all completed `SUCCESS`.

## Phase B — Stable proof schema

- [x] T410 Define repository-versioned proof schema major version 1.
- [x] T411 Emit explicit schema identity/version from `check --json`.
- [x] T412 Preserve existing proof meanings and exit-code semantics.
- [x] T413 Add policy-mode and policy-source provenance fields required by v1.
- [x] T414 Add deterministic schema/output contract tests and invalid-schema guard coverage.
- [x] T415 Document compatibility rules for schema major version 1.
- [ ] T416 Merge and verify the stable-schema unit canonically.

Phase B candidate contract:

- `schemas/proof-v1.json` defines exact ordered top-level fields, required fields, verdict/risk/verification states, and reserved policy modes;
- `check --json` prepends `schema=diffcipline.proof/v1`, `schema_version=1.0`, and explicit policy provenance while preserving the legacy evidence fields and exit-code mapping;
- `scripts/validate-proof-v1.py` parses real CLI output, requires exact schema field order and identity, and proves an incompatible schema version is rejected;
- CI runs the proof-v1 validator on Linux in addition to cross-platform Rust tests; the Rust runtime remains dependency-free;
- `docs/PROOF-CONTRACT.md` defines v1 compatibility and preserves PASS / REVIEW / FAIL / usage semantics.

## Phase C — Enterprise policy mode

- [ ] T420 Add explicit local enterprise-policy CLI input with no network discovery.
- [ ] T421 Enforce stricter numeric limits across enterprise and repository layers.
- [ ] T422 Enforce stricter dependency/lockfile/untracked decisions across layers.
- [ ] T423 Enforce cumulative forbidden surfaces and every non-empty expected-file contract.
- [ ] T424 Enforce cumulative deterministic verification commands and risk profiles.
- [ ] T425 Fail closed on malformed, unsupported, missing, or weakening layered policy states.
- [ ] T426 Expose enterprise-policy activation and source provenance in proof output.
- [ ] T427 Merge and verify enterprise policy mode canonically.

## Phase D — Broad agent portability

- [ ] T430 Publish a generic Agent Skills installation/portability contract.
- [ ] T431 Preserve one canonical `diffcipline` and `diffcipline-review` behavior across agents.
- [ ] T432 Qualify Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI from exact heads.
- [ ] T433 Add a generic layout/content qualification independent of one named client.
- [ ] T434 Document platform-neutral CLI/skill boundaries and limitations.
- [ ] T435 Merge and verify broad portability canonically.

## Phase E — Signed release-artifact contract

- [ ] T440 Define the v1 signed release-candidate artifact set and provenance contract.
- [ ] T441 Prove locked native builds for Linux, macOS, and Windows.
- [ ] T442 Prove deterministic SHA-256 manifest closure over all native binaries.
- [ ] T443 Prove GitHub/Sigstore provenance without repository-stored long-lived signing keys.
- [ ] T444 Verify attestation subjects against exact candidate binaries on trusted canonical pushes.
- [ ] T445 Document independent checksum and provenance verification.
- [ ] T446 Keep public tag/release creation outside the capability milestone unless separately authorized.
- [ ] T447 Merge and verify the signed release-artifact capability canonically.

## Phase F — Integrated qualification and closeout

- [ ] T450 Update README and contract docs only with implemented v1 capabilities.
- [ ] T451 Pass exact-head `ci`, `skills-compat`, `release`, and any dedicated v1 qualification gate on one final candidate.
- [ ] T452 Reconcile valid reviews/threads and reverify canonical `main` before merge.
- [ ] T453 Merge the final v1 capability candidate with an expected-head guard.
- [ ] T454 Verify exact post-merge repository, portability, schema/policy, and signed-release evidence.
- [ ] T455 Record `COMPLETE_CANONICAL` separately only after T454 is machine-observed and the terminal record itself becomes canonical.

## Ordering

T403 gates all implementation. T416 gates enterprise policy work. T427 gates final portability/release integration. T447 gates integrated closeout. T455 is terminal.
