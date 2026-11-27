"""Time conversion fixture for an OCR production smoke test."""


def minutes_to_seconds(minutes: int) -> int:
    """Convert whole minutes to seconds."""
    if minutes < 0:
        raise ValueError("minutes must be non-negative")
    return minutes * 60
