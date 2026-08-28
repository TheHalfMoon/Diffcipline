from datetime import datetime


def parse_timestamp(value: str) -> datetime:
    if value.endswith("Z"):
        raise ValueError("Z suffix is not supported")
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return parsed
