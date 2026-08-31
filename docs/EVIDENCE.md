# Diffcipline capability-to-evidence matrix

This document maps public capability statements to evidence that can be inspected or executed. It is not a comparative ranking and does not convert popularity into engineering quality.

## Product evidence

| Capability | Observable claim | Canonical evidence | Limitation |
| --- | --- | --- | --- |
| Deterministic proof | `diffcipline check` returns explicit PASS / REVIEW / FAIL from repository facts and policy rather than a model-generated quality score. | `docs/PROOF-CONTRACT.md`; CLI tests under `crates/diffcipline-cli/tests/` | A verdict is only as strong as the repository policy and verification commands it is given. |
| Exact-diff scope | Policy can bound changed-file count, added lines, dependency manifests, lockfiles, untracked files, expected paths, and forbidden surfaces. | `.diffcipline.toml`; `docs/PROOF-CONTRACT.md`; CLI policy tests | Diffcipline does not infer product intent from natural language when no explicit scope contract is configured. |
| Risk-aware verification | Explicit R0–R3 profiles select repository-declared verification and fail closed when a requested profile is absent or empty. | `docs/PROOF-CONTRACT.md`; CLI integration tests | Risk classification is supplied/configured; Diffcipline does not claim autonomous security risk classification. |
| Explicit execution | Configured commands execute only when `--run` is requested; otherwise missing evidence cannot become a clean PASS. | README two-minute proof; `crates/diffcipline-cli/tests/quickstart.rs`; `docs/PROOF-CONTRACT.md` | Repository verification commands are executable code and must be reviewed before use on untrusted changes. |
| Enterprise layering | A local enterprise baseline can be tightened by repository policy but not weakened. | `docs/ENTERPRISE-POLICY.md`; policy-layering tests | There is no remote policy service, credential exchange, or network policy discovery. |
| Portable Agent Skills | One canonical behavior is qualified across Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Gemini CLI, and the generic Agent Skills layout. | `docs/INSTALLATION.md`; `.github/workflows/skills-compat.yml` | Compatibility qualification proves repository layouts/install behavior, not vendor endorsement. |
| GitHub Action | The Action runs the same CLI contract, preserves exit status, writes proof to the job summary, and requires explicit verification execution. | `action.yml`; `.github/workflows/ci.yml`; README Action example | Production consumers should pin an immutable release or exact commit. |

## Release evidence

Public `v1.0.0` is fixed at commit `5cb1c77340b75649f6168e0e8f66479ea047ea96`.

GitHub release `379824838` is published with `draft=false`, `prerelease=false`, and immutable state. Its five-file closure is:

1. `diffcipline-aarch64-apple-darwin`
2. `diffcipline-x86_64-pc-windows-msvc.exe`
3. `diffcipline-x86_64-unknown-linux-gnu`
4. `SHA256SUMS`
5. `PROVENANCE.sigstore.json`

The publication chain and machine verification are preserved in:

- `docs/RELEASES.md` — release protocol;
- `specs/006-v1-publication/t632-published-verification.md` — published immutable verification evidence;
- recovery verifier run `33424987600`, job `99596275866` — successful fixed-lineage, immutability, checksum, attestation, and every-asset verification;
- evidence artifact `9770386235`, digest `sha256:1ecfe4b8e1bac7f66c56d14602ac655514b05b2b87816d2efe683867d6053db0`.

The first automatic `release.published` verifier failure remains documented. It was not erased or relabeled as success.

## Benchmark evidence

Diffcipline's published benchmarks do not currently establish a correctness advantage.

- `benchmarks/results/v0.1/REPORT.md`: baseline, Karpathy, Ponytail, and Diffcipline each finished at 1/6 correct in the canonical six-task experiment; executor/provider limitations are published.
- `benchmarks/results/v0.3/REPORT.md`: all treatments again finished at 1/6 task-correct in the accepted reference experiment; scorer confounding, provider/tool failures, timeouts, and limitations are preserved.
- `benchmarks/PROTOCOL.md`: defines the publication doctrine for future experiments, including raw outputs, scorers, failures, costs/tokens when available, and limitations.

These negative results are part of the public evidence surface and must remain visible in any future comparison or recommendation claim.

## Discovery metadata limitation

As observed on 2026-08-31, the live GitHub repository has no description, no topics, and no separate homepage. The authenticated execution surface available to this program exposes repository reads but no repository-metadata mutation action. Spec 007 therefore records this as an explicit administrative/tooling limitation rather than claiming a mutation that did not occur.

No homepage is proposed until a stable independent canonical destination exists; the GitHub repository remains the canonical landing surface.

## Claim discipline

Do not infer that Diffcipline is universally better than another project from this matrix. Comparative claims require the separately source-frozen Phase E method. Adoption signals such as stars, forks, installs, search ranking, or LLM mentions are observations, not engineering-quality evidence.
