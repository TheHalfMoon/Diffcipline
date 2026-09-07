# Acknowledgments and prior art

Diffcipline is an independent clean-room implementation. It does not vendor or copy the implementation text of the projects below.

## multica-ai/andrej-karpathy-skills

The project popularized a compact set of coding-agent behavioral principles around surfacing assumptions, avoiding over-engineering, making surgical changes, and defining verifiable success criteria.

Source: https://github.com/multica-ai/andrej-karpathy-skills

## DietrichGebert/ponytail

Ponytail demonstrated a strong minimal-solution ladder, broad agent portability, lifecycle integration, and the value of publishing reproducible benchmarks for behavioral skills.

Source: https://github.com/DietrichGebert/ponytail

## obra/superpowers

Superpowers is important prior art for treating software-development methodology as composable agent skills rather than a single monolithic prompt.

Source: https://github.com/obra/superpowers

## Tencent/SkillHone

SkillHone is relevant prior art for evidence-gated Agent Skill evolution. Its useful concepts for future Diffcipline work include persistent decision history, held-out regression validation, evaluation/skill separation, and treating the entire skill folder as the change surface rather than only `SKILL.md`.

Diffcipline does not adopt SkillHone's optimization harness, model-provider stack, local Git server, or self-evolution loop through this acknowledgment. Any future implementation inspired by these ideas requires separate repository authorization, a demonstrated verification benefit, compatibility with Diffcipline's portable Agent Skills core, and evidence that evaluation inputs cannot leak into the skill under test.

Qualified observation revision: `7d565839fb4dc74f9c77f09ace660e1c0484e048`

Source: https://github.com/Tencent/SkillHone

License observed at qualification: MIT.

## Tencent/LoopForge

LoopForge is relevant prior art for resumable software-delivery workflows. Its useful concepts for future Diffcipline work include risk-sensitive workflow routing, separation of implementation/review/testing responsibilities, persisted verification artifacts, and explicit handoff/resume state for interrupted agent work.

Diffcipline does not adopt LoopForge as a multi-agent orchestration framework through this acknowledgment. Future adoption should remain bounded to proof and verification concerns; Diffcipline should not require a workflow manager in order to use its core Agent Skill or CLI. Direct code reuse, if ever proposed, must preserve LoopForge and applicable third-party attribution requirements.

Qualified observation revision: `09c765286f549624dd95434e1e6ef2249657cbeb`

Source: https://github.com/Tencent/LoopForge

License observed at qualification: MIT, with third-party attribution requirements documented by the source repository.

## Agent Skills

Diffcipline follows the open Agent Skills directory convention so the behavioral layer remains portable across compatible agents and installers.

Source: https://agentskills.io/

## Attribution policy

Contributions must preserve attribution for directly adapted ideas and must comply with the source license when code or text is incorporated. Prefer independent implementations over copying. Benchmarks comparing other projects must be reproducible and fair.
