# Execution frontier — Spec 003

Live GitHub/repository truth overrides this snapshot.

## Terminal state

Spec 003 has no remaining implementation, experiment, publication, or closeout task after T265.

`COMPLETE_CANONICAL` becomes effective only when this terminal completion record is itself merged to canonical `main` and its required post-merge gates are machine-observed successful. Until then, this branch is only the completion candidate.

## Preserved canonical history

Spec 001 / v0.1 and Spec 002 / v0.2 are complete. The immutable `v0.1.0` tag remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

The canonical v0.1 benchmark remains unfavorable: every arm scored `1/6`, all arms changed zero files, Diffcipline was slowest, and no correctness advantage is supported. Invalid run `33195457215` remains excluded.

Spec 003 planning T200–T203 became canonical at `c392d372564b55cc7d55aee8bed1b2641dee6820`. Executor schema, adapter boundary, matrix/evidence orchestration, reproducibility qualification, containment, and the guarded real-experiment boundary became canonical through `234f007dc8765f7b7649ada7d7d1d00ae4c12538`.

## Accepted v0.3 experiment

The only authorized comparative execution ran once as `benchmark-v0.3-reference` run `33269484561` (#16) against exact canonical target `234f007dc8765f7b7649ada7d7d1d00ae4c12538` after qualification run `33269349342`.

Raw results artifact `9720290597` has digest `sha256:dcad221a52e110a34198109ac31bfe164e2ac47610e78b83b9d98f17102c3218`. Reservation artifact `9719653684` has digest `sha256:f63e381cb199a064b875cdaf25eba614f3ea9b38048cd20bfbc18a689d6e28b7`.

The accepted attempt contains 24 rows: 12 `included`, 12 `failed`, 0 `timed_out`, and 0 `excluded`. Every required run bundle is present; fixture base commits and comparison-contract digests match across treatments; runtime/model/treatment/sandbox provenance matches; qualification and containment passed; and no failed or losing result was selectively rerun.

All four treatments were `1/6` task-correct. The frozen scorer remained unchanged and reported `0/6` scorer-pass for every treatment because test-generated `__pycache__` files were counted as changed/unrelated/protected paths. All textual patches were empty. Nine failed rows ended in provider/tool-parser HTTP 500 errors and three in internal agent request timeouts. Tokens and monetary cost are unavailable. These limitations remain part of the published evidence.

## Publication and closeout

Publication records under `benchmarks/results/v0.3/` preserve the exact accepted artifact identity, provenance, metrics, failures, unavailable metrics, scorer limitation, packaging/checksum limitation, and finite artifact-retention boundary.

PR #54 final exact head `e5e3b2675af2af55426229dc4afbbb349db956d8` passed:

- `benchmark-v0.3-qualification` `33301772574`: SUCCESS;
- `skills-compat` `33301772570`: SUCCESS;
- `release` `33301772566`: SUCCESS;
- `ci` `33301772564`: SUCCESS;
- guarded `benchmark-v0.3-reference` validation `33301772610`: SUCCESS.

PR #54 had no submitted reviews or inline review threads and was expected-head squash-merged as canonical commit `d59cc6ec570c894713d6bf32aa0b4af9d60d7c38`.

Exact post-merge push gates on `d59cc6ec570c894713d6bf32aa0b4af9d60d7c38` were:

- `ci` `33301846572`: SUCCESS;
- `benchmark-v0.3-qualification` `33301846507`: SUCCESS;
- `skills-compat` `33301846603`: SUCCESS;
- `release` `33301846610`: SUCCESS.

T264 was machine-observed before this completion record was authored. T265 is therefore eligible to record terminal completion.

## No further Spec 003 work

Do not execute another v0.3 comparative experiment. Do not selectively rerun accepted tasks. Do not rewrite the scorer or accepted result boundary after observation. Do not create a v0.3 release tag. Do not implement v1.0 under Spec 003 authority.

After this completion record itself becomes canonical and its post-merge gates succeed, re-read canonical `main`, `AGENTS.md`, `CONSTITUTION.md`, `README.md`, and `specs/CURRENT.md`. Any next roadmap phase must establish a new canonical specification authority before implementation.
