# Execution frontier — Spec 006

Live GitHub/repository truth overrides this snapshot.

## Canonical publication chain

Spec 005 is `COMPLETE_CANONICAL` at `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`.

Spec 006 planning authority is canonical at `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577`.

The sole authorized `v1.0.0` release commit is `5cb1c77340b75649f6168e0e8f66479ea047ea96`. Its exact post-merge `ci` `33403468465`, `skills-compat` `33403468547`, and `release` `33403468550` completed `SUCCESS`.

Owner-only tag authority run `33403681664` fixed `v1.0.0` exactly at that SHA. Owner-only staging run `33403855005` created and byte-verified draft release `379824838` from the exact canonical signed release candidate with exactly five assets.

PR #73 canonically recorded tag/staging evidence at `e42bdccd7a97089fd986d478fadaf92b406d873d`. PR #74 canonically recorded the independent T630 administrator confirmation at `2444671549cb22fc664e6f3476dcb43cd964d28f`.

## Published immutable v1.0.0

The repository administrator published existing release `379824838` through GitHub's administrative release surface on 2026-08-31.

Live GitHub state reports:

- tag `v1.0.0`;
- `draft=false`;
- `immutable=true`;
- `prerelease=false`;
- `published_at=2026-08-31T18:17:06Z`;
- fixed tag target `5cb1c77340b75649f6168e0e8f66479ea047ea96`;
- exactly the same five staged assets.

T631 is complete.

## Preserved verifier failure and canonical recovery

The automatic `release.published` verifier run `33424164688` failed in job `99593546041` after lineage succeeded but before immutable-release verification. The exact failure was:

```text
accepts 1 arg(s), received 4
```

That failed run remains preserved publication evidence.

PR #76 corrected only the invalid `gh api --jq` / jq variable composition. Its exact head `90333921e06daeeae488f8fa97abdf55c886586b` passed all nine required pull-request workflows and was merged with expected-head protection to canonical recovery SHA `95efb154b93a4745e0265bb4e2b94b60cd1d0463`.

Exact post-merge recovery gates completed `SUCCESS`:

- `ci` `33424737598`;
- `skills-compat` `33424737542`;
- `release` `33424737688`.

## T632 machine verification

The repository owner then issued:

```text
/verify-release v1.0.0 5cb1c77340b75649f6168e0e8f66479ea047ea96
```

Recovery verifier run `33424987600`, job `99596275866`, completed `SUCCESS` and machine-proved:

- fixed tag lineage and recorded release SHA;
- crate version `1.0.0`;
- successful tag and staging authority evidence;
- `isDraft=false`;
- `isImmutable=true`;
- GitHub release-attestation verification;
- exact five-asset closure;
- three-entry `SHA256SUMS` closure and successful checksums;
- attestation verification for every native binary;
- release-asset verification for every published asset;
- durable uploaded verification evidence.

Evidence artifact `9770386235`, `v1.0.0-release-verification`, has digest `sha256:1ecfe4b8e1bac7f66c56d14602ac655514b05b2b87816d2efe683867d6053db0` and expires `2026-11-29T18:26:10Z`.

T632 is complete and is recorded in `t632-published-verification.md`.

## Terminal frontier — T633

There is no remaining publication implementation work.

Branch `docs/006-terminal-closeout` records terminal `COMPLETE_CANONICAL` status only after T632 was machine-observed. The status becomes effective only if:

1. the exact terminal head passes all required pull-request workflows;
2. review, thread, comment, mergeability, and canonical-main reconciliation are clean;
3. the PR is merged only with its expected head SHA;
4. the resulting canonical SHA passes exact post-merge `ci`, `skills-compat`, and `release`.

Until those conditions hold, this branch is only the terminal completion candidate. Once they hold, Spec 006 is `COMPLETE_CANONICAL` and the separate Spec 007 Category Leadership authority may be reconciled and activated.
