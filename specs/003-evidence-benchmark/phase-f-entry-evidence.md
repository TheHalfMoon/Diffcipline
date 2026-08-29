# Phase F entry evidence — Spec 003

This document records the machine-observed evidence required to close T250 and T251 before any v0.3 comparative model execution is authorized.

## Canonical target

- canonical `main`: `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea`
- PR #51 exact head: `82b701e43f3d64b57c9fc8da266cdc33489cdaf7`
- PR #51 merge commit: `f1f41f52a732230b39ac8cba082db262a0d58c9e`
- PR #52 exact head: `b089c4b06c41aa62848bf8a5ae9f5eb420f5d0f3`
- PR #52 merge commit: `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea`

## Pinned reference contract

`benchmarks/v0.3/experiment.json` on canonical `main` freezes one executor, one model/runtime lineage, one fixture revision, one prompt suffix, one sandbox contract, and four treatments.

Reference executor:

- executor id: `local-llama32-3b-q4km`
- adapter: `local-openai-tool-loop`
- runtime: `ggml-org/llama.cpp` release `b10621`
- runtime revision: `c1d0e7a004015f23bc0233470b747b596f29b264`
- runtime archive SHA-256: `91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583`
- model repository: `bartowski/Llama-3.2-3B-Instruct-GGUF`
- model revision: `54651d07cdbbd900b46c652cbf6672c935a22236`
- model file: `Llama-3.2-3B-Instruct-Q4_K_M.gguf`
- model SHA-256: `6c1a2b41161032677be168d354123594c0e6e67d2b9227c84f296ad037c728ff`
- model quantization: `Q4_K_M`
- fixture revision: `cde4d0058ce522ddd9863457c29560679fac53dd`
- per-task timeout: `480` seconds
- CPU limit: `4` cores
- memory limit: `16` GiB
- storage limit: `14` GiB

Treatment lineage:

- baseline: no skill
- Karpathy revision `2c606141936f1eeef17fa3043a72095b4765b9c2`, blob `6a62d0441753157ca6ca50479e490c2948033adb`
- Ponytail revision `2ed6c52c9d7e5e56942508591085fd45dea277d3`, blob `02c0712c86277d49d18a77da3a2b825657bf02d1`
- Diffcipline revision `6bbeb59bab21724c92ed3456953a94e5202f0e53`, blob `0ca69dc046c7ba41d9b361b734a776ff536695ac`

The guarded workflow cross-checks this v0.3 lineage against the frozen v0.1 source contract before any real execution.

## Real execution containment

The bash-tool environment is pinned to:

`python:3.12.11-slim-bookworm@sha256:519591d6871b7bc437060736b9f7456b8731f1499a57e22e6c285135ae657bf7`

The sandbox contract requires:

- Docker-backed isolated bash execution;
- `--network none`;
- read-only container root filesystem;
- only the disposable benchmark workspace mounted read-write;
- all Linux capabilities dropped;
- `no-new-privileges`;
- explicit CPU/memory/PID limits;
- `--pull=never` during agent tool execution;
- no Docker socket mount;
- no inherited GitHub credentials.

PR #51 exact-head qualification run `33263875174` was SUCCESS and its containment step was SUCCESS. Its qualification artifact was:

- artifact id: `9718040977`
- name: `v0.3-harness-qualification`
- digest: `sha256:f982a83cf9bfbff45ccbb5d7a1862e973e343de7845de3782161bcfff6ce71a6`

The artifact records exact head `82b701e43f3d64b57c9fc8da266cdc33489cdaf7`, 24 deterministic matrix rows, `private_credentials_required=false`, and `comparative_model_execution=false`.

## Exact-head verification

PR #51 exact head `82b701e43f3d64b57c9fc8da266cdc33489cdaf7` passed:

- `benchmark-v0.3-reference` `33263875157`: SUCCESS
- `benchmark-fixtures` `33263875156`: SUCCESS
- `benchmark-v0.3-qualification` `33263875174`: SUCCESS
- `ci` `33263875162`: SUCCESS
- legacy `benchmark-arms` `33263875194`: SUCCESS; regression-only, not v0.3 comparative evidence

PR #52 exact head `b089c4b06c41aa62848bf8a5ae9f5eb420f5d0f3` passed:

- `benchmark-v0.3-reference` `33264366591`: SUCCESS
- `benchmark-v0.3-qualification` `33264366617`: SUCCESS
- `benchmark-fixtures` `33264366590`: SUCCESS
- `ci` `33264366589`: SUCCESS

PR #52 had no submitted reviews and no inline review comments.

## Canonical post-merge verification

On canonical `main` `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea`:

- `benchmark-fixtures` `33264509821`: SUCCESS
- `benchmark-v0.3-qualification` `33264509832`: SUCCESS
- `ci` `33264510009`: SUCCESS

Canonical qualification artifact:

- artifact id: `9718225574`
- name: `v0.3-harness-qualification`
- digest: `sha256:2d9c782799b376b6c61ccb617941e4f7dbc6d93a1d7efa757c9d3794f2b2bd94`
- repository revision: `743f3295cc2cf597dfa5eb9b16ffac53cc8183ea`
- result: `PASS`
- matrix rows: `24`
- private credentials required: `false`
- comparative model execution: `false`
- Docker socket: absent
- network: denied
- root filesystem: read-only
- workspace write: verified
- private credentials exposed: `false`
- sandbox image id: `sha256:688a685f6a1fa9250d7c6cee916889cbca364e4b027520110e0fce80c64a13e0`

The artifact also preserves the frozen v0.1 preparer, scorer, and run-config blob identities.

## Conclusion

T250 and T251 are supported by exact-head and canonical post-merge machine evidence. The pinned runtime/model/treatment identities and the matched fixture/prompt/permissions/resource/sandbox contract are now canonical.

No v0.3 comparative model run is included in this evidence. T252 and T253 remain blocked until this T250/T251 completion record itself is merged and its exact post-merge gates are machine-observed. The only authorized real-experiment entry after that boundary is the guarded owner command defined by the canonical workflow.
