# Task

`parse_query` must correctly decode URL query strings:

- `+` means a space;
- percent escapes are decoded;
- repeated keys preserve all values in order;
- blank values are preserved.

Preserve the current `dict[str, list[str]]` API. Use only the Python standard library; do not add a dependency.

Run the repository tests before finishing.
