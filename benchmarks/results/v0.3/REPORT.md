# Diffcipline v0.3 benchmark evidence

## Result

The accepted v0.3 reference experiment does **not** show a correctness advantage for Diffcipline, Karpathy, or Ponytail. Under one pinned local executor, all four treatments finished at **1/6 task-correct**. The only correct fixture was the already-minimal no-op task (`f06`).

The frozen scorer reported **0/6 scorer-pass for every treatment**, but that signal is contaminated by a reproducible harness limitation: running the fixture tests generated `__pycache__` bytecode files, and the frozen scorer treated those untracked files as changed, unrelated, and protected paths. Every textual patch is empty and no source-text edit was observed. The scorer boundary is intentionally left unchanged after execution; this limitation is published rather than repaired post hoc.

With 1 success in 6 tasks, the Wilson 95% correctness interval is approximately **3.0% to 56.4%** for every treatment. This sample and the four-way correctness tie do not support a treatment-effect inference.

## Canonical execution

- Workflow: `benchmark-v0.3-reference` run `33269484561` (#16), conclusion `SUCCESS`
- Repository revision: `234f007dc8765f7b7649ada7d7d1d00ae4c12538`
- Attempt: `attempt-001`
- Qualification run: `33269349342`
- Results artifact: `9720290597`
- Results artifact SHA-256: `dcad221a52e110a34198109ac31bfe164e2ac47610e78b83b9d98f17102c3218`
- Reservation artifact: `9719653684`
- Reservation artifact SHA-256: `f63e381cb199a064b875cdaf25eba614f3ea9b38048cd20bfbc18a689d6e28b7`
- Canonical treatment order: baseline -> Karpathy -> Ponytail -> Diffcipline
- Matrix rows: 24
- Manifest: 12 included, 12 failed, 0 timed out, 0 excluded
- Selective reruns: none

| Treatment | Correct | Scorer pass | Included | Failed | Clean exits | Summed task seconds | Bash calls |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 1/6 | 0/6 | 5 | 1 | 5/6 | 494.365 | 41 |
| Karpathy | 1/6 | 0/6 | 3 | 3 | 3/6 | 902.187 | 61 |
| Ponytail | 1/6 | 0/6 | 1 | 5 | 1/6 | 700.243 | 41 |
| Diffcipline | 1/6 | 0/6 | 3 | 3 | 3/6 | 939.839 | 57 |

Diffcipline had the largest summed task duration in this run. No arm produced a source-text patch. The scorer reported 12 changed and 12 unrelated files per treatment solely because each of the six fixtures contained two generated Python bytecode cache files after verification.

## Failures and exclusions

Twelve matrix rows are explicitly `failed`. Nine ended with provider/tool-call parsing HTTP 500 errors and three ended with internal agent request timeouts that surfaced as executor exit `2`. The experiment manifest contains **no hidden exclusions** and **no manifest-level timed-out rows**; the internal timeout failures remain visible as failed rows because the outer arm process returned before its per-task timeout boundary.

No individual task or treatment was retried. Losing and failed transcripts, stderr/stdout, scorer outputs, patches, status, metadata, and workspaces remain in the exact raw artifact.

## Matching and provenance

All 24 rows use the same executor contract, model, prompt suffix, fixture revision, sandbox, permissions, timeouts, and resource limits. Base commits match across all four treatments for each fixture.

The pinned executor is `local-llama32-3b-q4km` using `llama.cpp` release `b10621` / source revision `c1d0e7a004015f23bc0233470b747b596f29b264`, model `bartowski/Llama-3.2-3B-Instruct-GGUF` revision `54651d07cdbbd900b46c652cbf6672c935a22236`, and digest-pinned `python:3.12.11-slim-bookworm` sandbox with network denied, read-only root filesystem, no Docker socket, and no exposed GitHub credentials.

Treatment source revisions and observed SHA-256 values are:

| Treatment | Source revision | Observed treatment SHA-256 |
| --- | --- | --- |
| Baseline | none | none |
| Karpathy | `2c606141936f1eeef17fa3043a72095b4765b9c2` | `6e22cc54cb02a5e98ae42d06d9d7292db0c1b43894831b32879beb0166b2aea7` |
| Ponytail | `2ed6c52c9d7e5e56942508591085fd45dea277d3` | `1316a2f3f95741d2300b116fe0c2d81ce4a9568656ed0a62643f54aaf09957f2` |
| Diffcipline | `6bbeb59bab21724c92ed3456953a94e5202f0e53` | `1ea34f6557ed259f8f653841f1fbc8bd82c370d52bd3036aa0371605a988312b` |

`MANIFEST.json`, `RUNTIME-PROVENANCE.json`, `QUALIFICATION.json`, `CONTAINMENT.json`, and the exact raw artifact provide the machine-auditable lineage.

## Checksum and packaging audit

The published `raw-canonical-evidence.zip` is the exact GitHub Actions artifact download and its SHA-256 exactly matches GitHub's recorded artifact digest.

The attempt-local `SHA256SUMS` inside that ZIP was generated before artifact packaging and contains 463 entries. GitHub Actions omitted 168 hidden `.git` files from ephemeral `work/` repositories while packaging the artifact. All 295 checksum entries whose files are present match exactly; no required per-run evidence bundle file is missing. The absent entries are Git metadata from duplicate ephemeral work directories, not transcripts, outputs, scores, patches, status, metadata, resulting workspaces, reservation, qualification, or provenance records.

This packaging mismatch is retained as a limitation. The repository-level `SHA256SUMS` checks the exact published raw ZIP and the extracted publication records rather than pretending the internal pre-packaging checksum list is self-contained.

## Metrics and limitations

Correctness and scorer-pass are reported separately. Because generated bytecode files trigger the frozen integrity logic, the v0.3 scorer-pass, changed-file, unrelated-churn, and protected-integrity signals are not useful evidence of a treatment effect in this run. Added/deleted source LOC and dependency additions are zero for every treatment; textual patches are empty.

Verification was classified as `some` for all 24 rows. Tokens and monetary cost are **NOT AVAILABLE** because the harness did not persist reliable usage/cost telemetry. The small pinned 3B Q4 model/runtime produced frequent provider/tool-parser failures and internal timeouts, so the experiment does not establish how these treatments would behave with a stronger executor.

## Raw evidence

The exact workflow artifact is published as `raw-canonical-evidence.zip`. It contains every accepted run bundle plus reservation, qualification, containment, runtime provenance, local-model logs, evidence validation, and the original experiment manifest.

```sh
cd benchmarks/results/v0.3
sha256sum -c SHA256SUMS
unzip -l raw-canonical-evidence.zip
```

No failed or losing result was removed, replaced, or selectively rerun.
