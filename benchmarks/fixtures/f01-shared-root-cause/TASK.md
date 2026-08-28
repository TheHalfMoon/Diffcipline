# Task

Sessions that expire exactly at `now` must already be treated as expired for every access check.

Keep the active-session rule in one place rather than fixing duplicated copies independently. Preserve the existing public API and revoked-session behavior.

Run the repository tests before finishing.
