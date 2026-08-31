# Execution frontier — Spec 006

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 005 is `COMPLETE_CANONICAL` at `e64a6ae9ad50edc9e08a1392c23134f96d4d7587` after terminal post-merge `ci` `33398836802`, `skills-compat` `33398836751`, and `release` `33398836807` all completed `SUCCESS`.

Spec 006 planning authority is canonical at `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577`. PR #69 exact head `2d633052e990b5ba852495eecb49d1b2a5d25ab6` passed `ci` `33399447630`, `skills-compat` `33399447639`, `release` `33399447636`, and every historical v0.1 guard. Exact post-merge `ci` `33399584260`, `skills-compat` `33399584290`, and `release` `33399584278` all completed `SUCCESS`; the canonical release run proved the three locked native builds, deterministic checksum closure, signed Sigstore provenance, and every binary attestation subject.

The only pre-v1 tag/release remains immutable historical `v0.1.0` at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

## Current Phase B candidate

The current implementation branch is limited to the version and guarded-tag authority surface:

- crate and lockfile version are `1.0.0`;
- `CHANGELOG.md` records only machine-proven v1 capabilities and keeps publication completion conditional on the immutable verifier;
- new `tag-v1.0.0.yml` accepts only the owner-authored exact `/release v1.0.0 <sha>` contract, requires `origin/main` to equal that SHA, requires successful exact-SHA canonical `ci`, `skills-compat`, and `release` push runs, refuses an existing tag, and creates a lightweight tag only at the verified SHA;
- `release.yml` now qualifies changes to the v1 tag authority;
- historical v0.1 PR validators resolve version `0.1.0` from the fixed immutable v0.1 tag instead of incorrectly requiring the current crate to remain at 0.1.0 forever.

No tag has been created and no release has been staged or published by this candidate.

## Next gates

Qualify this exact bounded candidate and make its version/tag-authority changes canonical. Then implement T612/T613 recovery staging and immutable published-release verification, complete T610 release documentation, and use that second unit as the final T614/T615 publication-implementation candidate.

T615 still gates any `v1.0.0` tag creation.
