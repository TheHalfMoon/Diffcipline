# Execution frontier — Spec 004

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 003 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its terminal post-merge `ci`, `benchmark-v0.3-qualification`, `skills-compat`, and `release` runs succeeded. No v0.3 release tag was created.

The v1 roadmap authority is the canonical README entry **Universal engineering governor**: stable proof schema, broad agent portability, signed release artifacts, and enterprise policy mode.

## Existing capability to preserve

- dependency-free Rust CLI with PASS / REVIEW / FAIL and JSON output;
- repository policy version 1 with diff limits, dependency/lockfile/untracked decisions, intent surfaces, and risk-specific verification;
- portable `diffcipline` and `diffcipline-review` Agent Skills;
- exact-head installation qualification for six named agent clients;
- locked Linux/macOS/Windows release builds, SHA-256 aggregation, GitHub/Sigstore attestation, and attestation verification on trusted pushes;
- all canonical v0.x benchmark and release evidence.

## Gaps this spec closes

- machine proof JSON has no stable schema identity/version contract;
- enterprise policy layering does not exist;
- portability evidence exists but lacks a generic v1 installation contract;
- signed candidate machinery exists but is not yet defined and qualified as the stable v1 release-artifact capability.

## Immediate frontier

The only authorized task before implementation is **T403**: make this planning authority canonical through exact-head review/gates, expected-head merge, and exact post-merge verification.

Do not modify CLI behavior, skills, release workflows, or v1 user-facing claims before T403 becomes canonical.

After T403, Phase B stable proof schema is the next authorized implementation unit. Enterprise policy work cannot begin until the schema unit is canonical.

## Stop conditions

Stop rather than weaken governance if canonical `main` moves unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, a proposed enterprise layer can weaken a baseline, schema changes silently reinterpret existing fields, portability requires divergent behavioral skill copies, signing requires a long-lived repository secret, or a public tag/release is proposed without separate irreversible-action authority.
