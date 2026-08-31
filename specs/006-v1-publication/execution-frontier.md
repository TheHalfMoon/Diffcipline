# Execution frontier — Spec 006

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 005 is `COMPLETE_CANONICAL` at `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`.

Spec 006 planning authority is canonical at `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577`.

The version/tag-authority unit is canonical at `a36f1fc867b2da565cd3168fa44f13aa9c1b8893` after PR #70 and exact post-merge `ci` `33401705271`, `skills-compat` `33401705118`, and `release` `33401705332` all completed `SUCCESS`.

T612 recovery staging is canonical at `1c95c1d8831054baa9510b709035ccf0b51c14d5`. PR #71 exact head `2ff1a7b1fd6c74b80dca0f2c849c52dda0524180` passed `ci` `33402523847`, `skills-compat` `33402523838`, `release` `33402523846`, `tag-v1.0.0` `33402523857`, `stage-v1.0.0-release` `33402524111`, and all historical v0.1 guards. Expected-head merge produced `1c95c1d8831054baa9510b709035ccf0b51c14d5`; exact post-merge `ci` `33402743391`, `skills-compat` `33402743395`, and `release` `33402743372` all completed `SUCCESS`. The canonical release run produced the signed candidate after three locked native builds, deterministic checksum closure, signed Sigstore provenance, and attestation-subject verification.

Canonical `main` therefore carries crate/lockfile version `1.0.0`, guarded `v1.0.0` tag authority, preserved immutable v0.1 validation, and owner-only draft recovery staging.

The only existing tag/release remains immutable historical `v0.1.0` at `ab434ae114b5f11ea9eb882bf572831dc7634531`. No `v1.0.0` tag or release exists at this frontier.

## Current final Phase B candidate

The current bounded unit finishes publication implementation by adding:

- an immutable `v1.0.0` published-release verifier that requires exact tag lineage and crate version, the tagged SHA recorded in release notes, successful tag/staging authority evidence, `isDraft=false`, `isImmutable=true`, and `gh release verify`;
- exact five-asset closure, three-entry checksum verification, every binary GitHub attestation, and `gh release verify-asset` for every published asset;
- 90-day machine-readable published-release verification evidence;
- `docs/V1_PUBLICATION.md`, which records the exact release-commit, tag, staging, administrator-immutability, publication, and re-verification contracts.

The verifier has no publication path. Repository automation still cannot publish the draft.

## Final qualification and release target

This candidate is the T614 qualification target. It must pass exact-head `ci`, `skills-compat`, `release`, v1 tag/staging/verifier validation, all historical v0.1 guards, and complete review/thread/comment, mergeability, and canonical-main reconciliation.

Only the exact qualified head may be merged. T615 requires successful exact post-merge `ci`, `skills-compat`, and `release` on the resulting canonical SHA. That T615 SHA becomes the sole authorized `v1.0.0` release target.

After T615, no implementation work is authorized before the guarded tag. A verified draft will still not authorize publication without independent administrator confirmation that GitHub release immutability is enabled.
