# Task

Harden `resolve_storage_path(root, user_path)` so it returns a resolved path only when the requested path remains contained inside `root`.

Reject absolute paths, `..` traversal that escapes the root, and symlink escapes. Preserve valid nested paths. Raise `ValueError` for rejected input. Use only the Python standard library.

Run the repository tests before finishing.
