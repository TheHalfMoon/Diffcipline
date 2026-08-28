---
name: diffcipline
description: Engineering discipline for coding agents. Use for coding, debugging, refactoring, implementation planning, or code changes when the goal is to reduce silent assumptions, avoid unnecessary code and dependencies, keep diffs surgical, scale verification with risk, and require evidence before declaring work done.
license: MIT
---

# Diffcipline

Apply this loop to coding work:

**Think → Challenge → Minimize → Change → Prove**

## 1. Think

Understand the request and the code path before editing.

- Surface assumptions only when they materially affect implementation.
- Trace the real flow and callers for bug fixes; fix the root cause when one shared fix is correct.
- If two interpretations produce meaningfully different implementations and repository truth cannot resolve them, say what is ambiguous.

Do not use “thinking” as a reason to stall on ordinary, reversible work when repository evidence provides a safe default.

## 2. Challenge

Before adding code, ask whether the requested outcome already exists or can be achieved with less machinery.

Prefer, in order:

1. no change
2. existing code/pattern
3. standard library
4. native platform capability
5. already-installed dependency
6. tiny local implementation
7. new dependency or abstraction only with evidence

Challenge means removing accidental complexity, not arguing against explicit requirements.

## 3. Minimize

Choose the smallest **correct blast radius**, not the fewest characters.

- Every changed file must trace to the task.
- No drive-by formatting or refactors.
- No interface/factory/configuration for a single known case without a demonstrated need.
- Do not add a dependency for functionality the repository or platform already provides adequately.
- Delete only code made obsolete by this change unless broader deletion is explicitly in scope.

Never minimize away validation at trust boundaries, security controls, accessibility, data-loss prevention, required error handling, or explicit requirements.

## 4. Change

Implement the root-cause solution in the repository's existing style.

Risk changes rigor:

- R0: non-behavioral
- R1: local behavior
- R2: shared contract/persistence/concurrency/public interface
- R3: auth/security/payments/migrations/destructive boundary

A high-risk change may still be a tiny diff; tiny does not mean safe.

## 5. Prove

Do not say PASS, fixed, complete, or equivalent without evidence from the exact change.

Prefer the repository's own checks. When Diffcipline CLI is installed:

```bash
diffcipline check --base <base-ref> --run
```

Report checks precisely:

- PASS only for checks that actually ran and succeeded.
- NOT RUN when the environment cannot execute a required check.
- REVIEW when evidence is incomplete or policy asks for human judgment.
- FAIL when a hard policy or verification command fails.

End coding work with a compact proof summary: files changed, verification run, and any remaining review item. Do not invent confidence scores.
