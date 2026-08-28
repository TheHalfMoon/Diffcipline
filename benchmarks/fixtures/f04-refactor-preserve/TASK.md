# Task

`normalize_first` and `normalize_last` currently duplicate the same normalization rule.

Consolidate that repeated normalization into one private rule while preserving both public functions and all existing behavior. Keep the change local; no unrelated cleanup.

Run the repository tests before finishing.
