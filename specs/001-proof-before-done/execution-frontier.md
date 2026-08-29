# Execution frontier — Spec 001

This document is the canonical continuation handoff for `001-proof-before-done`.

Live GitHub/repository truth always overrides this snapshot. Re-verify `main`, open pull requests, Actions runs, tags, releases, and the files in the read order below before acting.

## Canonical read order

1. `AGENTS.md`
2. `specs/CURRENT.md`
3. `specs/001-proof-before-done/spec.md`
4. `specs/001-proof-before-done/plan.md`
5. `specs/001-proof-before-done/tasks.md`
6. this file
7. `benchmarks/PROTOCOL.md`
8. `benchmarks/results/v0.1/REPORT.md`
9. `benchmarks/results/v0.1/MANIFEST.json`
10. `.github/workflows/ci.yml`
11. `.github/workflows/skills-compat.yml`
12. `.github/workflows/release.yml`
13. `.github/workflows/tag-v0.1.0.yml`
14. `.github/workflows/stage-v0.1.0-release.yml`
15. `.github/workflows/verify-v0.1.0-release.yml`
16. `docs/RELEASES.md`
17. `docs/v0.1.0-draft-staging-evidence.md`

## Last verified canonical state

Canonical `main` after the reviewed staging-recovery merge:

`528a1fd5a722bcd4c40e05b7e54a293c287e14b7`

The fixed v0.1 release commit and lightweight tag target remain:

`ab434ae114b5f11ea9eb882bf572831dc7634531`

Never move, replace, or recreate `v0.1.0`.

T062 exact canonical evidence on the release commit:

- `ci` push run `33237553577`: SUCCESS, including Rust and Diffcipline proof gates on Ubuntu, macOS, and Windows;
- `skills-compat` push run `33237553599`: SUCCESS for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI;
- `release` push run `33237553641`: SUCCESS, including canonical benchmark evidence validation, three locked native builds, SHA-256 aggregation, Sigstore provenance creation, and GitHub attestation verification.

T063 exact evidence:

- guarded tag-authority run `33237861972`: SUCCESS;
- lightweight `refs/tags/v0.1.0` resolves directly to `ab434ae114b5f11ea9eb882bf572831dc7634531`.

PR #28 staging-recovery exact candidate head `a36c5328231210ac3f1f6e5f4f21627b9f00e7d2` passed `ci`, `skills-compat`, `release`, tag validation, staging-recovery validation, and immutable-release-verifier validation before squash merge. The canonical recovery commit then passed `ci` run `33245573788`, `skills-compat` run `33245573759`, and `release` run `33245573820` on exact SHA `528a1fd5a722bcd4c40e05b7e54a293c287e14b7`.

## Canonical benchmark result

T001–T055 are complete through benchmark publication commit:

`78fcc432afcf0fabe2ed13800f7a9361570ab905`

Valid matched benchmark run `33200332207` used execution revision `b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc` and repaired fixture/preparer/scorer boundary `cde4d0058ce522ddd9863457c29560679fac53dd`.

| Arm | Correct | Scorer pass | Changed files | Total seconds |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 1/6 | 1/6 | 0 | 746.668 |
| Karpathy | 1/6 | 1/6 | 0 | 797.091 |
| Ponytail | 1/6 | 1/6 | 0 | 702.127 |
| Diffcipline | 1/6 | 1/6 | 0 | 981.263 |

The evidence does **not** show a correctness advantage for Diffcipline. Diffcipline was the slowest arm by observed total wall-clock time. The only correct fixture was the already-minimal no-op fixture `f06`. Run `33195457215` remains invalid comparative evidence. Never modify or selectively rerun benchmark evidence to improve the result.

## Verified draft staging

The intended tag-push `release.yml` path did not run after T063 because the guarded tag workflow pushed `v0.1.0` with the workflow `GITHUB_TOKEN`. GitHub suppresses new workflow runs caused by events created with that token, except explicit workflow/repository dispatch events. The tag itself is valid.

The reviewed recovery at `.github/workflows/stage-v0.1.0-release.yml` was merged canonically before use.

Owner staging request:

`/stage-release v0.1.0 ab434ae114b5f11ea9eb882bf572831dc7634531`

Staging recovery run `33245697424`: SUCCESS.

The workflow proved:

1. the request came from the repository owner;
2. `v0.1.0` still resolved to the fixed release commit;
3. the fixed release commit remained an ancestor of canonical `main`;
4. the tagged crate version remained exactly `0.1.0`;
5. the exact T062 run IDs were `33237553577`, `33237553599`, and `33237553641`;
6. the exact T063 tag-authority run was `33237861972`;
7. signed candidate artifact `9710422207` remained non-expired with digest `sha256:586ebf4c711b1d746e7664a1a71f4f2dd4542ee3eff98df2dfeb1443e4021e7e`;
8. the artifact contained exactly three native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`;
9. all three checksums and binary attestations verified;
10. no prior GitHub Release existed;
11. GitHub Release ID `378936458` was created as a draft;
12. all five uploaded draft assets were downloaded and byte-compared successfully.

Durable staging evidence:

- repository record: `docs/v0.1.0-draft-staging-evidence.md`;
- workflow artifact: `9712760016`;
- artifact digest: `sha256:22f6606a28900558a3a79c8782f44d3807f615346d356fb5613fbdc1ece20d18`;
- retention expiry: `2026-11-27T09:31:39Z`.

T064 is still open. A draft reporting `immutable=false` is not a failed immutable release because immutability must be proven after publication.

## Immutable publication authority and blocker

The draft is intentionally not published by repository automation. GitHub's repository immutable-release setting requires repository Administration access to inspect or change. Ordinary repository workflow tokens do not provide the required administrative authority.

The remaining authorized sequence is:

1. a repository administrator independently confirms **Enable release immutability** for `TheHalfMoon/Diffcipline`;
2. the administrator publishes the already-verified GitHub Release ID `378936458` without replacing assets or moving the tag;
3. the `release.published` event triggers `.github/workflows/verify-v0.1.0-release.yml`;
4. that verifier must succeed before T064 closes.

The verifier must machine-prove:

- the fixed tag still resolves to `ab434ae114b5f11ea9eb882bf572831dc7634531`;
- the tag target remains an ancestor of canonical `main`;
- crate version is `0.1.0`;
- `isDraft=false` and `isImmutable=true`;
- `gh release verify` succeeds;
- exactly five release assets are present;
- `SHA256SUMS` validates all three native binaries;
- each native binary verifies with `gh attestation verify`;
- every published asset verifies with `gh release verify-asset`;
- durable `v0.1.0-release-verification` workflow evidence is preserved.

The connected repository action surface available to this execution environment does not expose release publication or repository immutable-release administration. A read attempt against the repository immutable-release administrative endpoint is not supported by that connector surface. Do not convert missing administrative access into evidence that immutability is enabled or disabled.

## T065 completion contract

T065 remains open until the exact post-publication verifier evidence is committed and merged to canonical `main`. The final evidence change must remain within `.diffcipline.toml` limits and pass exact-head repository gates before merge.

Only after that final merge may `specs/CURRENT.md` and `tasks.md` record `COMPLETE_CANONICAL`.

## Stop conditions

Stop instead of weakening governance if:

- a required exact-head or canonical gate is missing or failing;
- a valid review finding remains unresolved;
- the fixed tag cannot remain constrained to the verified release SHA;
- the signed release artifact cannot be recovered or verified exactly;
- repository release immutability cannot be independently confirmed before publication;
- provenance, attestations, checksums, or published assets cannot be verified;
- post-publication evidence cannot be made canonical without bypassing repository rules.
