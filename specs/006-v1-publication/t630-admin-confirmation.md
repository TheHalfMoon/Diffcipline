# T630 — Administrator release immutability confirmation

Date: 2026-08-31

Status: `CONFIRMED_EXTERNAL_ADMIN_EVIDENCE`

## Administrator confirmation

An independent repository administrator supplied direct GitHub repository-settings evidence for `TheHalfMoon/Diffcipline` showing:

- repository **Settings** open on **General**;
- the **Releases** section visible;
- **Enable release immutability** selected;
- GitHub displaying the saved-state confirmation next to that setting.

This satisfies Spec 006 T630. The confirmation is external administrator evidence, not an inference from historical `v0.1.0` behavior and not a claim that repository automation can inspect the setting.

## Repository re-verification after confirmation

Live repository truth was rechecked after the administrator confirmation:

- canonical `main`: `e42bdccd7a97089fd986d478fadaf92b406d873d`;
- fixed `v1.0.0` tag target: `5cb1c77340b75649f6168e0e8f66479ea047ea96`;
- verified draft release: `379824838`;
- draft state remains `draft=true`, `prerelease=false`, `published_at=null`;
- the draft still contains exactly the three native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`.

`immutable=false` on the unpublished draft does not contradict the repository setting: Spec 006 requires immutable state to be proven after publication by the `release.published` verifier.

## Boundary after T630

T630 authorizes T631 but does not perform it.

The already-verified draft may now be published only through GitHub's administrative release surface. No repository workflow is authorized to publish it. T632 must then machine-prove `isDraft=false`, `isImmutable=true`, fixed tag lineage, release attestation, exact five-asset closure, checksums, binary attestations, and every release-asset verification before terminal T633 may become canonical.
