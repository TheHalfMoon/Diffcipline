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

## Last verified canonical state

Canonical `main` and the immutable v0.1 release commit at the start of this recovery are:

`ab434ae114b5f11ea9eb882bf572831dc7634531`

T062 exact canonical evidence on that SHA:

- `ci` push run `33237553577`: SUCCESS, including Rust and Diffcipline proof gates on Ubuntu, macOS, and Windows;
- `skills-compat` push run `33237553599`: SUCCESS for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI;
- `release` push run `33237553641`: SUCCESS, including canonical benchmark evidence validation, three locked native builds, SHA-256 aggregation, Sigstore provenance creation, and GitHub attestation verification.

T063 exact evidence:

- guarded tag-authority run `33237861972`: SUCCESS;
- lightweight `refs/tags/v0.1.0` resolves directly to `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Never move, replace, or recreate that tag.

T001–T055 are complete through the canonical benchmark publication at:

`78fcc432afcf0fabe2ed13800f7a9361570ab905`

The valid matched benchmark is `benchmark-arms` run `33200332207`, executed from canonical revision:

`b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc`

The repaired frozen fixture/preparer/scorer boundary is:

`cde4d0058ce522ddd9863457c29560679fac53dd`

Run `33195457215` is invalid comparative evidence because the old preparer produced different ephemeral fixture base commits across arms. It must never be counted as comparative benchmark evidence.

## Canonical benchmark result

| Arm | Correct | Scorer pass | Changed files | Total seconds |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 1/6 | 1/6 | 0 | 746.668 |
| Karpathy | 1/6 | 1/6 | 0 | 797.091 |
| Ponytail | 1/6 | 1/6 | 0 | 702.127 |
| Diffcipline | 1/6 | 1/6 | 0 | 981.263 |

The evidence does **not** show a correctness advantage for Diffcipline. Diffcipline was the slowest arm by observed total wall-clock time. The only correct fixture was the already-minimal no-op fixture `f06`. Preserve this losing result exactly.

Durable evidence is published under `benchmarks/results/v0.1/`:

- `MANIFEST.json`
- `REPORT.md`
- `SHA256SUMS`
- `raw-canonical-evidence.tar.gz`

## Active closeout state

T060–T063 are complete. T064 is active. T065 is not reached.

The intended `release.yml` tag-push path did not run after T063 because the guarded tag workflow pushed `v0.1.0` with the workflow `GITHUB_TOKEN`. GitHub suppresses new workflow runs caused by events created with that token, except explicitly dispatched workflow/repository events. The tag creation itself succeeded and remains valid; the missing tag-triggered run is an orchestration defect, not failed release evidence.

The recovery must not delete or replace the tag, rerun the benchmark, or substitute different release bytes.

## Change-size policy

The canonical `.diffcipline.toml` sets `max_added_lines = 400` and `max_changed_files = 12`. This recovery must independently satisfy that policy. Do not weaken the policy to land release automation.

## Release staging recovery authority

`.github/workflows/stage-v0.1.0-release.yml` is the repository-native recovery for the already-created `v0.1.0` tag. It is authorized only after review and canonical merge.

The owner request is exactly:

`/stage-release v0.1.0 ab434ae114b5f11ea9eb882bf572831dc7634531`

The workflow must fail closed unless it proves:

1. the request came from the repository owner on a pull-request conversation;
2. the requested SHA is the existing `v0.1.0` tag target;
3. the tagged release commit remains an ancestor of canonical `main`;
4. the tagged crate version is exactly `0.1.0`;
5. exact-SHA successful T062 runs exist for `ci.yml`, `skills-compat.yml`, and `release.yml`;
6. the successful T063 tag-authority run exists for the tagged SHA;
7. the non-expired `signed-release-candidate` artifact from exact T062 release run is unique and downloadable;
8. that artifact contains exactly three native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`;
9. the checksum manifest validates all three binaries and every binary verifies with `gh attestation verify`;
10. no GitHub Release already exists for `v0.1.0`.

Only then may it create a **draft** GitHub Release from those already-signed bytes. It must download the draft assets again, prove the exact five-file set is byte-identical, and preserve `v0.1.0-draft-staging-evidence` for 90 days.

## Immutable release authority

The draft is intentionally not published by repository automation. GitHub's repository immutable-release setting requires repository Administration access to inspect or change, while the ordinary workflow `GITHUB_TOKEN` does not receive that permission. A `403 Resource not accessible by integration` cannot be interpreted as evidence that immutability is enabled or disabled.

Before final T064 publication, a repository administrator must independently confirm that **Enable release immutability** is active and publish the already-verified draft through GitHub's administrative release surface. This is a genuine external administrative prerequisite.

Publication triggers `.github/workflows/verify-v0.1.0-release.yml`. Because post-tag evidence commits may advance `main`, the verifier must prove that the fixed tag target remains an ancestor of canonical `main`; it must never require moving the tag to the later evidence commit.

That exact release-event workflow must machine-prove:

- `v0.1.0` still resolves to the fixed release commit and its crate version is `0.1.0`;
- the tag target remains an ancestor of canonical `main`;
- `isDraft=false` and `isImmutable=true`;
- a valid GitHub Release attestation via `gh release verify`;
- exactly five release assets;
- `SHA256SUMS` validates all three native binaries;
- each native binary verifies with `gh attestation verify`;
- every published asset verifies with `gh release verify-asset`;
- a durable `v0.1.0-release-verification` Actions artifact records release metadata, tag SHA, canonical `main` SHA, workflow run ID, and published asset digests.

T064 is not complete if any of those post-publication checks fail or are absent.

T065 remains open until exact post-tag and post-publication evidence is committed and merged to canonical `main`. Only then may `specs/CURRENT.md` and the task ledger record `COMPLETE_CANONICAL`.

## Stop conditions

Stop instead of weakening governance if:

- any required exact-head or post-merge gate is missing or failing;
- a valid review finding remains unresolved;
- the tag cannot remain constrained to the verified release SHA;
- the canonical signed release artifact cannot be recovered and verified exactly;
- repository release immutability cannot be independently confirmed before publication;
- provenance, attestations, checksums, or published assets cannot be verified;
- post-tag evidence cannot be made canonical without bypassing repository rules.

No benchmark fixture, preparer, scorer, treatment, or result may be selectively changed or rerun to improve the published v0.1 outcome.
