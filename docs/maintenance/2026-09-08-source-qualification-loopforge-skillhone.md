# LoopForge and SkillHone source-qualification maintenance unit

Date: 2026-09-08

## Authorization

This is a separately authorized maintenance unit following canonical completion of Specs 001–008. The maintainer supplied Tencent/LoopForge and Tencent/SkillHone as candidate sources for Diffcipline and explicitly authorized proceeding with their project fit evaluation.

This maintenance unit does not reopen, extend, or replace any completed specification.

## Intent

Record reproducible prior-art qualification for the two supplied sources without changing Diffcipline runtime behavior, proof semantics, Agent Skill behavior, CLI behavior, workflows, dependencies, benchmark evidence, or release contents.

## Sources observed

### Tencent/SkillHone

Repository: https://github.com/Tencent/SkillHone

Observed revision: `7d565839fb4dc74f9c77f09ace660e1c0484e048`

Observed license: MIT.

Qualified concepts for future consideration:

- persistent decision history for skill changes;
- held-out regression validation before accepting an improvement;
- evaluation/skill isolation to reduce leakage;
- whole-skill verification across `SKILL.md`, scripts, references, and related skill assets.

Not adopted by this unit:

- autonomous skill optimization;
- provider/model gateway machinery;
- Forgejo or another local Git server;
- model credentials or runtime dependencies;
- any code, prompt text, benchmark result, or comparative claim from SkillHone.

### Tencent/LoopForge

Repository: https://github.com/Tencent/LoopForge

Observed revision: `09c765286f549624dd95434e1e6ef2249657cbeb`

Observed license: MIT with source-documented third-party attribution requirements.

Qualified concepts for future consideration:

- risk-sensitive routing between lightweight and stronger verification paths;
- separation of implementation, review, and testing responsibilities;
- persisted verification artifacts;
- explicit resume/handoff state for interrupted agent work.

Not adopted by this unit:

- a multi-agent orchestration framework;
- host-specific installation machinery;
- workflow-state implementation;
- any code, prompt text, third-party component, or comparative claim from LoopForge.

## Fit decision

`Tencent/SkillHone` is qualified as primary prior art for future Agent Skill verification and evolution work because its evidence, regression, and isolation concerns align directly with Diffcipline's proof-before-done model.

`Tencent/LoopForge` is qualified as supporting prior art for future resumability, role separation, and evidence-lifecycle work. It must not turn Diffcipline into a required multi-agent workflow manager or weaken the portable Agent Skills core.

Qualification means "relevant source worth considering under future authorization." It does not mean the source is adopted, vendored, benchmark-proven superior, or incorporated into Diffcipline.

## Authorized scope

- update `ACKNOWLEDGMENTS.md` with bounded prior-art attribution and adoption boundaries;
- record this source-qualification maintenance unit.

## Explicitly out of scope

- implementation changes of any kind;
- Agent Skill, CLI, GitHub Action, workflow, schema, or policy behavior changes;
- dependency, manifest, or lockfile changes;
- benchmark execution or comparison claims;
- copying source code or implementation text;
- new product claims or claims of superiority;
- changes to completed Specs 001–008;
- release, tag, asset, or provenance changes.

## Verification and completion rule

This is a documentation-only maintenance surface. Completion requires the exact pull-request head to pass every workflow selected by GitHub for these changed paths, clean reconciliation of reviews, threads, comments, mergeability, exact head, and canonical `main`, expected-head merge, and success of every workflow selected by GitHub for the resulting canonical push.

A workflow not selected by GitHub for these paths is not represented as `PASS`.

Until those conditions are machine-observed, this source qualification remains a candidate and canonical `main` remains authoritative.
