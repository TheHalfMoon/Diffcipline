# Changelog

## Unreleased

## 0.1.0 — 2026-08-29

### Added
- Initial open Agent Skills for implementation and review discipline.
- Dependency-free Rust CLI with `init` and deterministic `check` proof cards.
- PASS / REVIEW / FAIL verdict contract where NOT RUN never becomes PASS.
- Repository policy for diff size, dependency manifests, lockfiles, untracked files, and explicit verification commands.
- Risk model, proof contract, GitHub Action proof gate, cross-platform release workflow, and installer compatibility verification.
- Public six-task falsification benchmark with pinned model/runtime provenance and durable raw evidence.

### Benchmark
- Canonical matched run `33200332207` used repository revision `b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc` and repaired frozen fixture/preparer/scorer boundary `cde4d0058ce522ddd9863457c29560679fac53dd`.
- Baseline, Karpathy, Ponytail, and Diffcipline each scored `1/6` correct and `1/6` scorer-pass with zero changed files.
- Diffcipline had the largest observed total wall-clock time (`981.263s`) versus baseline (`746.668s`), Karpathy (`797.091s`), and Ponytail (`702.127s`).
- The tested 3B Q4 model/agent showed substantial tool/parser instability, so the experiment does not support a treatment-effect inference.
- Raw evidence, checksums, invalidated/excluded attempts, and limitations are published in `benchmarks/results/v0.1/`.
