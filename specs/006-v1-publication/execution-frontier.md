# Execution frontier — Spec 006

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 005 is `COMPLETE_CANONICAL` at `e64a6ae9ad50edc9e08a1392c23134f96d4d7587` after terminal post-merge `ci` `33398836802`, `skills-compat` `33398836751`, and `release` `33398836807` all completed `SUCCESS`.

Spec 006 planning authority is canonical at `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577`.

The first Phase B implementation unit is canonical at `a36f1fc867b2da565cd3168fa44f13aa9c1b8893`. PR #70 exact head `cb760c9a37a9168b5d9947b5927e1c8cb2095746` passed `ci` `33401308999`, `skills-compat` `33401309458`, `release` `33401308837`, `tag-v1.0.0` `33401308830`, and all historical v0.1 guards. Expected-head merge produced `a36f1fc867b2da565cd3168fa44f13aa9c1b8893`; exact post-merge `ci` `33401705271`, `skills-compat` `33401705118`, and `release` `33401705332` all completed `SUCCESS`. The canonical release run proved all three locked native builds, deterministic checksum closure, signed Sigstore provenance, and every binary attestation subject.

Canonical `main` now carries crate and lockfile version `1.0.0`, the v1 changelog entry, guarded `v1.0.0` tag authority, and preserved immutable v0.1 validation.

The only existing tag/release remains immutable historical `v0.1.0` at `ab434ae114b5f11ea9eb882bf572831dc7634531`. No `v1.0.0` tag or release exists at this frontier.

## Current Phase B staging candidate

The current bounded unit implements only T612 recovery staging plus its canonical evidence bookkeeping:

- owner-only request contract `/stage-release v1.0.0 <exact-release-sha>`;
- exact tag target, canonical-main ancestry, and crate-version verification;
- exact-SHA successful canonical `ci`, `skills-compat`, and `release` evidence plus successful v1 tag-authority evidence;
- exactly one non-expired `signed-release-candidate` selected from the resolved canonical release run;
- dynamic artifact ID/digest recording rather than hard-coded future artifact identity;
- exact five-file closure, three-entry `SHA256SUMS`, checksum verification, and every binary attestation verification;
- refusal to replace an existing release;
- draft-only creation with the exact release SHA recorded in release notes;
- complete five-asset round-trip byte comparison and 90-day staging evidence.

No path in this workflow publishes a release.

## Policy-preserving split

A combined T612 + T613 + runbook candidate measured `+473` lines, exceeding `.diffcipline.toml` `max_added_lines = 400`. The implementation is therefore split into separate canonical units rather than increasing or weakening repository policy.

After T612 becomes canonical, the final bounded unit will add T613 immutable published-release verification and finish T610 publication documentation. That final unit will be the T614 exact-head candidate and, after expected-head merge plus post-merge qualification, the T615 canonical release commit.

T615 still gates any `v1.0.0` tag creation. A verified draft will still not authorize publication without the independent administrator immutability prerequisite.
