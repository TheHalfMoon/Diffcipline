# Plan — 004 Universal Engineering Governor

## Delivery principles

- stabilize contracts before adding enterprise behavior;
- reuse the existing dependency-free CLI, Agent Skills layout, and Sigstore release path;
- make enterprise layering monotonic and local-file only;
- prove portability through one shared skill contract rather than per-agent forks;
- keep irreversible tag/public-release actions outside this milestone unless separately authorized;
- use exact-head and post-merge machine evidence for every canonical boundary.

## Phase A — Canonical planning

Establish Spec 004 authority, scope, task order, and explicit non-goals from the completed Spec 003 state and README v1.0 roadmap. No v1 implementation begins before this planning authority is canonical.

## Phase B — Stable proof schema

Version the machine proof as schema major version 1. Add a repository-tracked machine-readable schema and deterministic contract tests. Preserve existing field meanings and exit semantics. Include policy-mode/source provenance so later enterprise enforcement does not require an incompatible schema rewrite.

The human proof card remains concise and backward-compatible; schema stability applies to machine output, not whitespace of the human renderer.

## Phase C — Enterprise policy mode

Add an explicit CLI option for one enterprise baseline file. Load it only when requested. Evaluate enterprise and repository policies as independent layers, then enforce the strictest combined result without allowing the repository layer to weaken enterprise limits, decisions, scope restrictions, or required verification.

Do not add remote fetching, credentials, discovery services, policy servers, or identity/RBAC machinery.

## Phase D — Broad agent portability

Publish one installation/portability contract covering the six already-qualified agent clients plus the generic Agent Skills layout. Strengthen `skills-compat` so it validates the shared contract from exact heads and detects accidental platform-specific divergence.

Do not create agent-specific copies of `SKILL.md`.

## Phase E — Signed release-artifact contract

Promote the existing locked multi-platform build, SHA-256 manifest, and GitHub/Sigstore attestation path into an explicit v1 release-candidate contract. Add qualification that proves exact checkout, three host binaries, checksum closure, signed provenance on trusted pushes, and subject verification.

A public tag or release remains outside this phase unless separately authorized after the canonical v1 capability milestone.

## Phase F — Integrated qualification and closeout

Update README/contract documentation only after the capabilities exist. Run the strongest exact-head gates on one final candidate, reconcile valid review findings, verify canonical `main`, merge with an expected-head guard, then verify exact post-merge CI/skills/release evidence.

Author a separate completion record only after post-merge capability and signed-provenance evidence are machine-observed.

## Ordering

A → B → C → D → E → F.

Stable schema work precedes enterprise provenance fields. Enterprise behavior must be canonical before final portability/release claims. No phase may weaken v0.x proof, benchmark, or release guarantees.
