# Current specification

Active candidate: [`004-universal-engineering-governor`](004-universal-engineering-governor/spec.md)

Status: `PLANNING`

Implementation is not authorized until Spec 004 planning authority is merged to canonical `main` and its exact post-merge gates succeed. Live GitHub/repository truth overrides this file.

## Canonical read order

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. `README.md` roadmap
4. this file
5. `specs/004-universal-engineering-governor/spec.md`
6. `specs/004-universal-engineering-governor/plan.md`
7. `specs/004-universal-engineering-governor/tasks.md`
8. `specs/004-universal-engineering-governor/execution-frontier.md`
9. current proof/policy/skills/release contracts relevant to the active task.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its terminal completion record became canonical after PR #55 and exact post-merge runs `ci` `33302411448`, `benchmark-v0.3-qualification` `33302411430`, `skills-compat` `33302411434`, and `release` `33302411442` all completed `SUCCESS`.

The accepted v0.3 reference experiment remains exactly one canonical execution: run `33269484561` against target `234f007dc8765f7b7649ada7d7d1d00ae4c12538`, raw artifact `9720290597`, digest `sha256:dcad221a52e110a34198109ac31bfe164e2ac47610e78b83b9d98f17102c3218`. It contains 24 rows: 12 included, 12 failed, 0 timed out, 0 excluded. Every treatment was `1/6` task-correct; no correctness advantage was established. Published limitations remain canonical and must not be rewritten.

## Spec 004 planning authority

The README v1.0 roadmap defines **Universal engineering governor** through four capabilities:

- stable proof schema;
- broad agent portability;
- signed release artifacts;
- enterprise policy mode.

Spec 004 deliberately stabilizes and layers the existing system rather than introducing a remote control plane or platform-specific forks. The CLI remains dependency-free by default, enterprise policy is local-file and monotonic, portability uses the shared Agent Skills contract, and signed candidate artifacts continue to use locked builds plus GitHub/Sigstore provenance.

## Immediate frontier

Only T403 is authorized: merge the Spec 004 planning authority and verify exact post-merge gates. No v1 implementation begins before T403 is canonical.

A public v1 tag/release is not authorized merely by this planning candidate. It is an irreversible boundary separate from the v1 capability milestone.
