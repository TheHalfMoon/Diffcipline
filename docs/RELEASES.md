# Release verification

Diffcipline release artifacts are built from locked Cargo inputs. The canonical v0.1 release candidate was built on the exact tagged commit, combined into a deterministic SHA-256 manifest, and signed with GitHub/Sigstore provenance before the tag was created.

## v1 signed release-candidate capability contract

Spec 004 v1 defines a **release-candidate capability**, not a public v1 release. The contract promotes the repository's existing `.github/workflows/release.yml` machinery into an explicit qualification surface without authorizing creation or movement of a v1 tag, draft release, or published release.

### Capability status

The v1 signed release-candidate capability is implemented and qualified on canonical `main`. Trusted canonical pushes exercise the locked three-platform build, deterministic checksum closure, keyless GitHub/Sigstore provenance, and attestation-subject verification before a signed candidate is accepted. This status does not imply that a public `v1.0` tag or GitHub release exists.

### Candidate artifact sets

A pull-request qualification run produces the `release-candidate` artifact with exactly four files:

- one `diffcipline-<rust-host>` binary built on Linux;
- one `diffcipline-<rust-host>` binary built on macOS;
- one `diffcipline-<rust-host>.exe` binary built on Windows;
- `SHA256SUMS`, containing exactly one sorted SHA-256 entry for each of those three binaries.

The manifest closes over the three native binaries only. It does not hash itself and it does not contain a provenance-bundle entry.

A trusted canonical push additionally produces `signed-release-candidate` with exactly five files:

- the same three host-native binaries;
- the same `SHA256SUMS` closure over those binaries;
- `PROVENANCE.sigstore.json`, the Sigstore bundle emitted from the GitHub artifact attestation.

Pull requests intentionally do not receive signing permissions. A PR can therefore qualify exact checkout, locked native builds, packaging, checksum closure, and verification tooling, while trusted canonical push evidence is required to qualify signing and attestation-subject verification.

### Build and checksum invariants

Every accepted v1 candidate must satisfy all of the following:

1. every build job checks out the exact candidate SHA and verifies `git rev-parse HEAD` before building;
2. all three native binaries are built with `cargo build --release --locked --package diffcipline`;
3. each packaged binary executes `--help` successfully on its host runner before upload;
4. the aggregate job downloads all three host artifacts with digest-mismatch failure enabled;
5. `SHA256SUMS` is generated in deterministic filename order and contains exactly three entries;
6. `sha256sum -c SHA256SUMS` succeeds before the candidate artifact is accepted.

The candidate is incomplete if any host build, checksum entry, or checksum verification is missing. A successful build on one platform cannot substitute for another platform.

### Keyless provenance invariants

On a trusted push, the release workflow uses GitHub OIDC and `actions/attest` to sign provenance from the exact `SHA256SUMS` subjects. The attestation job receives short-lived `id-token: write` authority and does not read a repository-stored private signing key.

The workflow must then:

1. preserve the emitted bundle as `PROVENANCE.sigstore.json`;
2. run `gh attestation verify` against every `diffcipline-*` binary in the signed candidate;
3. fail if any declared binary is not a valid subject of the repository's GitHub artifact attestation;
4. upload the complete five-file `signed-release-candidate` only after subject verification succeeds.

Repository-stored long-lived signing credentials are outside this contract and are not required for v1 provenance.

### Independent verification

After downloading one complete candidate directory on a Unix-like system, verify byte integrity with:

```bash
sha256sum -c SHA256SUMS
```

For a trusted signed candidate, verify all native binary subjects with a current GitHub CLI:

```bash
for file in diffcipline-*; do
  gh attestation verify "$file" --repo TheHalfMoon/Diffcipline
done
```

On PowerShell, the checksum manifest can be verified independently without trusting the build script:

```powershell
Get-Content SHA256SUMS | ForEach-Object {
  $parts = $_ -split '\s+', 2
  $expected = $parts[0].ToLowerInvariant()
  $path = $parts[1].Trim().TrimStart('*')
  $actual = (Get-FileHash -Algorithm SHA256 $path).Hash.ToLowerInvariant()
  if ($actual -ne $expected) { throw "SHA-256 mismatch: $path" }
}
```

Checksum verification proves that the downloaded binaries match the declared manifest. GitHub/Sigstore attestation verification independently binds each binary digest to the repository's trusted GitHub Actions identity. Neither check is a substitute for reviewing the source change when source correctness matters to the threat model.

### Public-release boundary

Spec 004 Phase E and its integrated closeout do **not** authorize a public v1 tag or release. The `stage GitHub release draft` job is expected to remain skipped on branch and `main` push qualification because it is guarded by `refs/tags/v*`.

Creating or moving a v1 tag, staging a v1 GitHub release, or publishing a v1 release is a separate irreversible release decision that requires its own explicit canonical authority. Successful v1 capability qualification must not be presented as evidence that a public v1 release exists.

### Evidence and retention boundary

GitHub Actions candidate artifacts have finite retention and are qualification evidence rather than permanent public distribution. The durable repository contract is the workflow plus canonical machine-observed run evidence. A later authorized public release would need its own immutable publication and verification evidence rather than relying on an expired workflow artifact.

## Release artifacts

A published release contains exactly five assets:

- one `diffcipline-<rust-host>` binary from Linux;
- one `diffcipline-<rust-host>` binary from macOS;
- one `diffcipline-<rust-host>.exe` binary from Windows;
- `SHA256SUMS` covering the three binaries;
- `PROVENANCE.sigstore.json`, the signed Sigstore attestation bundle generated by GitHub.

The release path refuses to stage a release when the tag does not equal `v<crate version>` from `crates/diffcipline-cli/Cargo.toml`.

## Verify checksums

On a Unix-like system, download the binaries and `SHA256SUMS` into one directory and run:

```bash
sha256sum -c SHA256SUMS
```

On PowerShell, compare each expected digest in `SHA256SUMS` with `Get-FileHash -Algorithm SHA256`.

A checksum proves that downloaded bytes match the release manifest. It does not by itself prove who produced the manifest.

## Verify signed provenance

With a current GitHub CLI:

```bash
gh attestation verify ./diffcipline-<rust-host> --repo TheHalfMoon/Diffcipline
```

Run the command for the binary you downloaded. Verification checks the GitHub artifact attestation that cryptographically binds the artifact name and SHA-256 digest to the GitHub Actions build identity.

The release workflow uses `actions/attest` with GitHub OIDC. Public-repository attestations are signed with a short-lived Sigstore-issued certificate and stored in GitHub's attestations API. No long-lived signing key is stored in this repository.

## Trust boundary

A valid checksum and attestation do not make arbitrary code safe. They establish release integrity and provenance: the bytes match the declared digest, and the digest was attested by the repository's GitHub Actions identity.

Review release notes, source changes, and repository policy when the change itself matters to your threat model.

## Pipeline behavior

- Pull requests build all three host-native binaries and verify the combined checksum manifest, but do **not** receive signing permissions.
- Trusted pushes to `main` additionally create and verify signed artifact attestations. This exercises the signing path before a release tag is created.
- An independently authenticated `v*` tag push can run `.github/workflows/release.yml`, repeat the build/checksum/provenance path, and stage a draft release.
- The repository-native `v0.1.0` tag authority uses the workflow `GITHUB_TOKEN`. GitHub suppresses new workflow runs caused by events created with that token, except explicit workflow/repository dispatch events, so the successful guarded tag push did not create a second tag-push `release` run.
- `v0.1.0` therefore uses the reviewed `.github/workflows/stage-v0.1.0-release.yml` recovery. It recovers the already-signed `signed-release-candidate` from exact canonical T062 release run `33237553641`, verifies tag lineage, T062/T063 run evidence, checksums, binary attestations, and the exact five-file set, then creates and byte-verifies a **draft** release. It does not rebuild a different candidate or move the tag.
- No repository workflow publishes the draft. This prevents automation from accidentally creating a mutable public release when the repository-level immutable-release setting cannot be inspected with the ordinary `GITHUB_TOKEN`.
- After an administrator independently confirms **Enable release immutability** in repository settings, that administrator publishes the already-verified draft through GitHub's administrative release surface.
- Publication triggers `.github/workflows/verify-v0.1.0-release.yml`, which fails unless the release is immutable, the fixed tag target remains an ancestor of canonical `main`, the crate version is `0.1.0`, the release attestation verifies, all five assets are present, the three binary checksums verify, every binary provenance attestation verifies, and every published asset verifies against the GitHub Release attestation.
- The verifier preserves a 90-day `v0.1.0-release-verification` workflow artifact for the post-tag canonical evidence PR.

Third-party Actions are pinned to exact commit SHAs. Release staging and verification use the GitHub CLI already present on GitHub-hosted runners rather than a third-party release action.

## v0.1 tag authorization

The connected repository tooling does not expose direct Git-tag mutation, so `v0.1.0` uses the reviewed repository-native authority in `.github/workflows/tag-v0.1.0.yml`.

The canonical v0.1 release commit is:

```text
ab434ae114b5f11ea9eb882bf572831dc7634531
```

Before tag creation, that exact commit passed successful `push` runs of `ci.yml`, `skills-compat.yml`, and `release.yml`, including signed provenance verification. Guarded tag-authority run `33237861972` then created lightweight `v0.1.0` directly at that SHA. The workflow never replaces an existing tag, and the existing tag must not be moved or recreated.

## v0.1 staging recovery authorization

After the staging-recovery workflow is reviewed and canonical, the repository owner may post exactly:

```text
/stage-release v0.1.0 ab434ae114b5f11ea9eb882bf572831dc7634531
```

The workflow fails closed unless the request comes from the repository owner, the existing tag still resolves to that exact SHA, the tagged commit remains an ancestor of canonical `main`, exact successful T062/T063 runs exist, and the unique non-expired `signed-release-candidate` artifact from the exact T062 release run can be recovered and fully verified.

Only after those checks pass may it create a draft release. It then downloads the draft assets and byte-compares them with the recovered signed candidate, and preserves `v0.1.0-draft-staging-evidence` for 90 days.

## Immutable publication authorization

GitHub's repository-level immutable-release setting requires repository Administration access to inspect or modify. The ordinary workflow `GITHUB_TOKEN` deliberately used by this repository does not receive that administrative permission. Repository automation therefore does not treat an administrative `403 Resource not accessible by integration` as evidence that immutability is enabled or disabled.

There is deliberately no repository workflow that can publish the draft.

Before T064 publication, a repository administrator must independently confirm in GitHub repository settings that **Enable release immutability** is active and then publish the existing `v0.1.0` draft through GitHub's administrative release surface. That publication is an external administrative prerequisite, not an ordinary repository automation step.

The resulting `release.published` event must make `.github/workflows/verify-v0.1.0-release.yml` succeed. The machine proof includes:

```bash
gh release view v0.1.0 --repo TheHalfMoon/Diffcipline --json isDraft,isImmutable
gh release verify v0.1.0 --repo TheHalfMoon/Diffcipline
gh release verify-asset v0.1.0 <asset> --repo TheHalfMoon/Diffcipline
gh attestation verify <binary> --repo TheHalfMoon/Diffcipline
sha256sum -c SHA256SUMS
```

`isDraft` must be `false`, `isImmutable` must be `true`, the release attestation must verify, all five release assets must verify, and the three binaries must match both `SHA256SUMS` and their GitHub artifact attestations. T064 is not complete until that exact post-publication workflow succeeds.
