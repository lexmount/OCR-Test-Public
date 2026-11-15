"""Small review progress helper used by the isolated OCR rollout tests."""

def completed_ratio(completed: int, total: int) -> float:
    """Return completed/total; an empty batch is fully complete.

    Counts must satisfy 0 <= completed <= total. Partial progress must retain
    its fractional component so a half-complete batch reports 0.5.
    """
    if total < 0 or completed < 0 or completed > total:
        raise ValueError("invalid review counts")
    return completed / total if total else 1.0
