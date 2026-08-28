# Implementation plan — 001 Proof Before Done

## Architecture

The v0.1 core has two independent layers:

1. **Behavioral layer** — `skills/diffcipline/SKILL.md` and `skills/diffcipline-review/SKILL.md`.
2. **Evidence layer** — a dependency-free Rust CLI that reads Git and repository policy.

The skill can be used without the CLI. The CLI can inspect a repository without an LLM. Their combination creates the closed loop.

## CLI modules for v0.1

The initial implementation may remain in one source file until a second stable responsibility boundary emerges. Premature module splitting is explicitly avoided.

Responsibilities:
- command parsing;
- policy parsing;
- Git diff/status collection;
- dependency and lockfile classification;
- verification command execution;
- proof rendering in human and JSON formats.

## Security

Verification commands are repository-provided executable material. `check` is read-only by default. Commands execute only with `--run`. Documentation must tell users to review policy before running an untrusted repository.

## Compatibility

- Linux, macOS, and Windows through Rust standard library process APIs.
- Git is required.
- Shell execution uses `sh -lc` on Unix and `cmd /C` on Windows.

## Deferred decisions

- stable JSON schema versioning;
- signed proof artifacts;
- GitHub Action annotation UX;
- expected-file proof contracts;
- risk-path inference;
- release package managers.
