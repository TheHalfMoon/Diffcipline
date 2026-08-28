from pathlib import Path


def resolve_storage_path(root: str | Path, user_path: str) -> Path:
    return Path(root) / user_path
