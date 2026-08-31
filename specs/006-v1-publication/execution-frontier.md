# Execution frontier — Spec 006

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 005 is `COMPLETE_CANONICAL` at `e64a6ae9ad50edc9e08a1392c23134f96d4d7587` after terminal post-merge `ci` `33398836802`, `skills-compat` `33398836751`, and `release` `33398836807` all completed `SUCCESS`.

Canonical release run `33398836807` built locked Linux/macOS/Windows binaries, generated and verified deterministic `SHA256SUMS`, created signed Sigstore provenance, preserved the attestation bundle, verified every native-binary subject, and intentionally skipped GitHub release drafting because no authorized v1 tag existed.

No open pull request was present when Spec 006 planning began. The only tag was immutable historical `v0.1.0` at `ab434ae114b5f11ea9eb882bf572831dc7634531`, and the only published release was immutable `v0.1.0`.

The crate and lockfile still declare version `0.1.0`.

## Publication reality

The existing generic `release.yml` can build, checksum, attest, and stage a draft on an independently authenticated `v*` tag push, but repository-native tag creation through the workflow `GITHUB_TOKEN` does not generate a second tag-push release run. Therefore v1 publication needs explicit guarded tag authority plus recovery staging from the exact canonical signed candidate.

Repository automation deliberately cannot publish a draft. Administrative confirmation that GitHub release immutability is enabled remains an external prerequisite before publication.

## Immediate frontier — Phase A

T603 is next: qualify and merge this publication planning authority, then verify exact post-merge `ci`, `skills-compat`, and `release` on canonical `main`.

No version bump, tag creation, draft release, or publication is authorized before T603 becomes canonical.
