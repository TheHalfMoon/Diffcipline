def normalize_first(value: str) -> str:
    return " ".join(value.strip().split()).casefold()


def normalize_last(value: str) -> str:
    return " ".join(value.strip().split()).casefold()


def same_person(first_a: str, last_a: str, first_b: str, last_b: str) -> bool:
    return (
        normalize_first(first_a) == normalize_first(first_b)
        and normalize_last(last_a) == normalize_last(last_b)
    )
