# Security

## Reporting

Please report suspected vulnerabilities privately to the repository owner rather than opening a public exploit report.

## Trust boundary

`.diffcipline.toml` may contain verification commands. Diffcipline treats those commands as executable repository content.

- `diffcipline check` does not execute them.
- `diffcipline check --run` does.
- Review the policy before running `--run` in an untrusted repository.
- CI should pin trusted actions and minimize token permissions.

Diffcipline must never label an unexecuted verification command as PASS.
