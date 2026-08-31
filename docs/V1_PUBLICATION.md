# v1.0.0 publication runbook

This runbook is subordinate to `specs/006-v1-publication/spec.md` and live GitHub truth. It does not authorize a tag, draft, or publication by itself.

## Release commit

The v1 release commit is the exact canonical `main` SHA produced by T615 after the complete publication implementation is merged. Before any tag exists, that SHA must have successful exact-SHA `push` runs of:

- `ci.yml`;
- `skills-compat.yml`;
- `release.yml`.

The successful canonical `release.yml` run must contain one non-expired `signed-release-candidate` artifact with exactly five files: three host-native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`.

## Guarded tag

From a pull-request conversation, the repository owner may request exactly:

```text
/release v1.0.0 <exact-40-hex-canonical-sha>
```

`.github/workflows/tag-v1.0.0.yml` fails closed unless the requested SHA is still exact canonical `main`, crate version is `1.0.0`, required exact-SHA push qualification is successful, and `v1.0.0` does not already exist. The workflow never replaces or moves an existing tag.

## Verified draft staging

After the tag authority succeeds, the repository owner may request exactly:

```text
/stage-release v1.0.0 <exact-40-hex-release-sha>
```

`.github/workflows/stage-v1.0.0-release.yml` verifies tag lineage, crate version, exact canonical CI/skills/release evidence, successful tag authority, and the unique non-expired `signed-release-candidate` from the selected exact-SHA release run. It verifies the five-file closure, checksums, and every binary attestation before creating a **draft** release.

The workflow then downloads the draft and byte-compares all five assets with the verified canonical candidate. It refuses to replace an existing release and cannot publish the draft.

## Administrative immutability boundary

Repository automation deliberately does not infer the repository-level immutable-release setting from inaccessible administration APIs.

Before publication, a repository administrator must independently confirm in GitHub repository settings that **Enable release immutability** is active. Only then may that administrator publish the already-verified `v1.0.0` draft through GitHub's administrative release surface.

No repository workflow is authorized to publish the draft.

## Published release verification

Publication must trigger `.github/workflows/verify-v1.0.0-release.yml`. The verifier fails unless:

- `v1.0.0` resolves to the recorded release SHA and remains an ancestor of canonical `main`;
- crate version at the tag is `1.0.0`;
- the release body records the exact tagged SHA;
- successful tag and staging authority runs exist for that release SHA;
- the release is not a draft and reports `isImmutable=true`;
- `gh release verify v1.0.0` succeeds;
- exactly five assets exist;
- `SHA256SUMS` has exactly three entries and verifies all three binaries;
- `gh attestation verify` succeeds for every binary;
- `gh release verify-asset` succeeds for every published asset.

The verifier retains `v1.0.0-release-verification` evidence for 90 days.

For an explicit re-verification after publication, the repository owner may post:

```text
/verify-release v1.0.0 <exact-40-hex-release-sha>
```

A verified draft is not a published release. Spec 006 is not complete until the immutable published-release verifier succeeds and terminal evidence becomes canonical.
