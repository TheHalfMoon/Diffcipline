# Spec 006 — v1 Public Publication

## Status

`COMPLETE_CANONICAL`

This terminal status is effective only after this completion record is merged to canonical `main` and the required exact post-merge `ci`, `skills-compat`, and `release` gates succeed on the resulting canonical SHA. Until those conditions hold, this branch is only the terminal completion candidate.

Spec 005 remains `COMPLETE_CANONICAL`. This specification did not reopen or reinterpret any completed capability work.

## Authority and purpose

Diffcipline entered this specification with a canonical, machine-qualified v1 capability set and release-candidate pipeline, but no public v1 release. Spec 006 authorized only the irreversible publication sequence required to publish `v1.0.0` from an exact canonical commit while preserving proof-before-done and the repository's immutable-release boundary.

The authorized sequence was limited to:

1. set the crate/package version to `1.0.0` and update the lockfile and public changelog/release documentation consistently;
2. add narrowly scoped repository-native guarded authority for creating immutable tag `v1.0.0` at one exact canonical SHA only after exact-SHA canonical qualification succeeds;
3. add recovery staging that can create a draft `v1.0.0` release only from the exact non-expired `signed-release-candidate` produced by that canonical SHA;
4. preserve the five-asset release contract: three host-native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`;
5. require external repository-administrator confirmation that GitHub release immutability is enabled before publishing the verified draft;
6. verify the published release through a `release.published` or guarded recovery workflow that proves immutable state, fixed tag lineage, crate version, release attestation, asset count, checksums, binary attestations, and release-asset attestations;
7. record terminal publication evidence only after the published-release verifier succeeds.

## Version and canonical release commit contract

The public release version is exactly `1.0.0` and the tag is exactly `v1.0.0`.

The sole release commit is `5cb1c77340b75649f6168e0e8f66479ea047ea96`. Its exact post-merge `ci` `33403468465`, `skills-compat` `33403468547`, and `release` `33403468550` completed `SUCCESS` before tag creation.

The existing `v0.1.0` tag and immutable release remain untouched.

## Tag authority contract

The v1 tag workflow:

- validates its request contract on pull requests;
- accepts only an exact owner-authored `/release v1.0.0 <40-hex-sha>` request on a pull-request conversation;
- verifies exact checkout, crate version `1.0.0`, exact equality between `origin/main` and the requested SHA, and successful exact-SHA canonical `ci`, `skills-compat`, and `release` push runs;
- refuses to replace or move any existing `v1.0.0` tag;
- creates a lightweight tag only at the verified canonical SHA.

Owner-only run `33403681664` created `v1.0.0` exactly at the authorized release SHA.

## Draft staging contract

Because GitHub suppresses workflow events created with the repository workflow `GITHUB_TOKEN`, a separate owner-triggered recovery staging workflow was used.

Staging run `33403855005`:

- accepted only `/stage-release v1.0.0 <40-hex-sha>` from the repository owner;
- verified the existing tag, lineage, crate version, exact canonical workflow evidence, and tag-authority evidence;
- resolved the exact non-expired canonical `signed-release-candidate`;
- verified its five-file closure, `SHA256SUMS`, and every native-binary attestation;
- created draft release `379824838` only;
- downloaded that draft and byte-compared every staged asset with the canonical signed candidate;
- retained machine-readable staging evidence.

No repository workflow published the draft.

## Immutable publication contract

An independent repository administrator confirmed in GitHub repository settings that **Enable release immutability** was active before publication. That evidence is recorded in `t630-admin-confirmation.md`.

The administrator then published the already-verified draft through GitHub's administrative release surface. Release `379824838` now reports:

- tag `v1.0.0`;
- `draft=false`;
- `immutable=true`;
- `prerelease=false`;
- `published_at=2026-08-31T18:17:06Z`;
- the same exact five staged assets.

## Published-release verification contract

The published-release verifier was required to fail unless all of the following were true:

- release tag is `v1.0.0` and resolves to the recorded release SHA;
- tagged SHA remains an ancestor of canonical `main`;
- crate version at the tag is `1.0.0`;
- release is not a draft and reports `isImmutable=true`;
- `gh release verify v1.0.0` succeeds;
- exactly five published assets exist;
- `SHA256SUMS` contains exactly three entries and verifies all native binaries;
- `gh attestation verify` succeeds for every native binary;
- `gh release verify-asset` succeeds for every published asset;
- durable workflow evidence records the tag SHA, canonical main SHA, publication metadata, and verifier run identity.

The first automatic `release.published` run `33424164688` failed before immutable-release verification because of invalid `gh api --jq` argument composition. That failure remains preserved evidence.

PR #76 corrected only the verifier mechanics and became canonical at `95efb154b93a4745e0265bb4e2b94b60cd1d0463` after exact post-merge `ci` `33424737598`, `skills-compat` `33424737542`, and `release` `33424737688` completed `SUCCESS`.

Owner-triggered recovery verifier run `33424987600`, job `99596275866`, then completed `SUCCESS` and proved every published-release requirement above. Durable evidence artifact `9770386235`, `v1.0.0-release-verification`, has digest `sha256:1ecfe4b8e1bac7f66c56d14602ac655514b05b2b87816d2efe683867d6053db0`. The full machine-observed record is preserved in `t632-published-verification.md`.

## Preservation and non-goals

Spec 006 preserved:

- dependency-free Rust CLI behavior and all proof/policy contracts;
- Agent Skills portability and existing GitHub Action behavior;
- frozen benchmark evidence and all immutable historical release evidence;
- signed release-candidate construction and provenance semantics.

It did not add product features, dependencies, benchmark reruns, dashboards, telemetry, package-registry publication, auto-update mechanisms, or any automated draft-publication path.

## Qualification

Every repository change remained subject to `.diffcipline.toml` policy and the strongest exact-head gates for its touched surface. The final release implementation passed exact candidate qualification and exact post-merge release-commit qualification before tag creation. Subsequent tag, staging, administrator, verifier-recovery, and published-release evidence were separately qualified and preserved.

## Completion evidence

T632 was machine-observed before this terminal record was authored:

- published release `379824838` is immutable and not a draft;
- fixed tag `v1.0.0` remains at `5cb1c77340b75649f6168e0e8f66479ea047ea96`;
- recovery verifier run `33424987600`, job `99596275866`, completed `SUCCESS`;
- the verifier proved fixed lineage, exact authority evidence, immutable release attestation, five-asset closure, checksums, native-binary attestations, every release-asset verification, and durable evidence;
- artifact `9770386235` records the verification with digest `sha256:1ecfe4b8e1bac7f66c56d14602ac655514b05b2b87816d2efe683867d6053db0`.

Spec 006 has no remaining publication implementation frontier after this terminal record becomes canonical with successful required post-merge gates.

Only after this `COMPLETE_CANONICAL` status becomes effective may a separate canonical specification activate post-v1 Category Leadership work.
