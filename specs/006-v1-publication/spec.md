# Spec 006 — v1 Public Publication

## Status

`PLANNING_CANDIDATE`

This specification becomes publication implementation authority only after this planning record is merged to canonical `main` and the required exact post-merge `ci`, `skills-compat`, and `release` gates succeed on the resulting canonical SHA.

Spec 005 remains `COMPLETE_CANONICAL`. This specification does not reopen or reinterpret any completed capability work.

## Authority and purpose

Diffcipline now has a canonical, machine-qualified v1 capability set and release-candidate pipeline, but no public v1 release. This specification authorizes only the irreversible publication sequence required to publish `v1.0.0` from an exact canonical commit while preserving proof-before-done and the repository's immutable-release boundary.

The authorized sequence is limited to:

1. set the crate/package version to `1.0.0` and update the lockfile and public changelog/release documentation consistently;
2. add narrowly scoped repository-native guarded authority for creating immutable tag `v1.0.0` at one exact canonical SHA only after exact-SHA canonical qualification succeeds;
3. add recovery staging that can create a draft `v1.0.0` release only from the exact non-expired `signed-release-candidate` produced by that canonical SHA;
4. preserve the five-asset release contract: three host-native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`;
5. require external repository-administrator confirmation that GitHub release immutability is enabled before publishing the verified draft;
6. verify the published release through a `release.published` workflow that proves immutable state, fixed tag lineage, crate version, release attestation, asset count, checksums, binary attestations, and release-asset attestations;
7. record terminal publication evidence only after the published-release verifier succeeds.

## Version and canonical release commit contract

The public release version is exactly `1.0.0` and the tag is exactly `v1.0.0`.

The release commit must be a canonical `main` SHA whose exact push runs of `ci`, `skills-compat`, and `release` completed successfully after the version/publication implementation was merged. The guarded tag authority must fail closed unless canonical `main` still equals the requested target SHA when the tag is created.

The existing `v0.1.0` tag and immutable release remain untouched.

## Tag authority contract

The connected execution tooling does not expose direct Git-tag mutation. Repository-native tag authority therefore remains an explicit owner-triggered workflow.

The v1 tag workflow must:

- validate its request contract on pull requests;
- accept only an exact owner-authored `/release v1.0.0 <40-hex-sha>` request on a pull-request conversation;
- verify exact checkout, crate version `1.0.0`, exact equality between `origin/main` and the requested SHA, and successful exact-SHA canonical `ci`, `skills-compat`, and `release` push runs;
- refuse to replace or move any existing `v1.0.0` tag;
- create a lightweight tag only at the verified canonical SHA.

## Draft staging contract

Because GitHub suppresses workflow events created with the repository workflow `GITHUB_TOKEN`, the tag-authority push cannot be assumed to trigger the tag-push release workflow. A separate owner-triggered recovery staging workflow is therefore authorized.

The staging workflow must:

- accept only `/stage-release v1.0.0 <40-hex-sha>` from the repository owner;
- verify the existing tag resolves to the requested SHA, the tagged commit remains an ancestor of current canonical `main`, and the crate version is `1.0.0`;
- resolve successful exact-SHA canonical `ci`, `skills-compat`, and `release` evidence plus the successful v1 tag-authority run;
- require exactly one non-expired `signed-release-candidate` artifact from the exact canonical release run;
- download that artifact, require exactly five files, verify `SHA256SUMS`, and verify every binary attestation;
- refuse to replace any existing `v1.0.0` release;
- create a draft release only, then download it and byte-compare every staged asset with the verified canonical signed candidate;
- retain machine-readable staging evidence.

No repository workflow may publish the draft.

## Immutable publication contract

Publication is authorized only after a repository administrator independently confirms in GitHub repository settings that **Enable release immutability** is active. Ordinary repository automation and its `GITHUB_TOKEN` must not infer that administrative setting from lack of access.

The administrator may then publish the already-verified draft through GitHub's administrative release surface. The publication event must trigger the v1 verifier.

If the execution environment cannot inspect the administrative setting or publish through that administrative surface, it must stop at the verified draft and report the external administrative prerequisite rather than weakening this contract.

## Published-release verification contract

The v1 verifier must fail unless all of the following are true:

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

## Preservation and non-goals

Preserve:

- dependency-free Rust CLI behavior and all proof/policy contracts;
- Agent Skills portability and existing GitHub Action behavior;
- frozen benchmark evidence and all immutable historical release evidence;
- signed release-candidate construction and provenance semantics.

Do not add product features, dependencies, benchmark reruns, dashboards, telemetry, package-registry publication, auto-update mechanisms, or any automated draft-publication path.

## Qualification

Each repository change must stay within `.diffcipline.toml` policy and pass the strongest existing exact-head gates for its touched surface. Publication implementation must pass one final exact candidate head through `ci`, `skills-compat`, `release`, historical `v0.1.0` guards, review/thread/comment reconciliation, mergeability, and canonical-main reconciliation before expected-head merge. The resulting canonical release commit must then pass exact post-merge `ci`, `skills-compat`, and `release` before tag creation.

## Completion rule

Spec 006 is complete only after `v1.0.0` is published as an immutable release and the exact published-release verification workflow succeeds, followed by a terminal canonical evidence record.

A verified draft is an authorized intermediate state, not completion.
