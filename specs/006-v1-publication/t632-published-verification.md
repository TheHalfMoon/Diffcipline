# T632 — Published immutable v1.0.0 verification

Date: 2026-08-31

Status: `VERIFIED_MACHINE_EVIDENCE`

## Published release

GitHub release `379824838` is the published `v1.0.0` release for fixed tag target:

`5cb1c77340b75649f6168e0e8f66479ea047ea96`

Live publication state observed before verification:

- `draft=false`;
- `immutable=true`;
- `prerelease=false`;
- `published_at=2026-08-31T18:17:06Z`;
- exactly the five previously staged assets remain present.

## Preserved initial verifier failure

The automatic `release.published` run `33424164688` failed in job `99593546041` before immutable-release verification because the workflow incorrectly passed jq variable arguments through `gh api --jq`.

The exact failure was:

```text
accepts 1 arg(s), received 4
```

That failed run remains part of the publication history and was not relabeled or removed.

## Canonical recovery qualification

PR #76 exact head `90333921e06daeeae488f8fa97abdf55c886586b` corrected only the verifier command composition and publication ledger. All nine required pull-request workflows completed `SUCCESS` before expected-head merge.

Expected-head merge produced canonical recovery commit `95efb154b93a4745e0265bb4e2b94b60cd1d0463`.

Exact post-merge push gates on that SHA completed `SUCCESS`:

- `ci` run `33424737598`;
- `skills-compat` run `33424737542`;
- `release` run `33424737688`.

## Recovery verification

The repository owner then issued:

```text
/verify-release v1.0.0 5cb1c77340b75649f6168e0e8f66479ea047ea96
```

`verify-v1.0.0-release` recovery run `33424987600` completed `SUCCESS`. Job `99596275866` machine-proved:

- fixed tag lineage and recorded release SHA;
- crate version `1.0.0`;
- successful tag and staging authority evidence;
- `isDraft=false`;
- `isImmutable=true`;
- successful GitHub release-attestation verification;
- exact five-asset closure;
- three-entry `SHA256SUMS` closure and successful checksum verification;
- successful attestation verification for every native binary;
- successful release-asset verification for every published asset;
- durable canonical release-verification evidence.

Evidence artifact:

- name: `v1.0.0-release-verification`;
- artifact ID: `9770386235`;
- digest: `sha256:1ecfe4b8e1bac7f66c56d14602ac655514b05b2b87816d2efe683867d6053db0`;
- retention expiration: `2026-11-29T18:26:10Z`.

T632 is therefore machine-observed complete. This evidence authorizes only terminal T633 closeout; it does not reopen or mutate the immutable release.
