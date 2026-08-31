# Execution frontier — Spec 005

Live GitHub/repository truth overrides this snapshot.

## Current state

Spec 004 is `COMPLETE_CANONICAL` at terminal canonical `768bfcd48a1bbcc86e6ccbe879f87677eb66afb7` with no remaining implementation task.

Spec 005 planning authority is canonical at `3e7abe3ca7c95fe327ef04ccb46fae89286ab8bc`. Exact post-merge `ci` `33397182736`, `skills-compat` `33397182730`, and `release` `33397182737` all completed `SUCCESS`, so Phase B implementation is authorized.

Public-release publication remains outside Spec 005.

## Machine-reproduced parser defect

PR #67 began with test-only head `c20a81b9bf47ac3b7da55db6300385b8e25e706f`.

On that exact head, `ci` `33397575574` proved the pre-fix defect: Ubuntu and macOS passed format and clippy, then failed `cargo test --workspace --all-targets --locked`; dogfood proof verification also failed. The red regression requires quoted verification commands containing commas to survive as one array element.

## Current implementation candidate

The branch now contains:

- a surgical standard-library-only, quote-aware separator scan in the shared policy array parser;
- retained positive comma-preservation and negative fail-closed regression tests;
- explicit enterprise-enforcement documentation stating that `--enterprise-policy <path>` is effective only when supplied and that mandatory organization policy requires an externally controlled CI path that supplies it;
- a live repository-hygiene review recording an empty GitHub description, no issue-template directory, no supported description/topics mutation in the available authorized tooling, and no justification for adding process-only templates.

No dependency manifest or lockfile is changed.

## Next canonical gate

T515: qualify one final exact PR head with `ci`, `skills-compat`, `release`, historical immutable-release guards, submitted-review/inline-thread/technical-comment reconciliation, mergeability, and canonical-main verification. Only that qualified expected head may proceed to T516 merge and post-merge verification.
