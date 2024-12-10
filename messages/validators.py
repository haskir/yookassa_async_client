def check_metadata(value: dict) -> dict:
    if value is None:
        return {}
    if len(value) > 16:
        raise ValueError("Metadata must be less than 16 items")
    for key, value in value.items():
        if not isinstance(key, str):
            raise ValueError(f"Metadata key '{key}' must be a string")
        if len(key) > 32:
            raise ValueError(f"Metadata key '{key}' must be less than 32 characters")
        if len(str(value)) > 512:
            raise ValueError(f"Metadata value '{value}' must be less than 512 characters")
    return value


def check_transfers(value: list) -> list:
    if value is None:
        return []
    if len(value) > 100:
        raise ValueError("Transfers must be less than 100 items")
    return value
