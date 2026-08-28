def parse_query(raw: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    if not raw:
        return result
    for part in raw.split("&"):
        key, _, value = part.partition("=")
        result.setdefault(key, []).append(value)
    return result
