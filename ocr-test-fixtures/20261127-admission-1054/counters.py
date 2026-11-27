"""Counter fixture for an OCR production smoke test."""


def total_counts(counts: list[int]) -> int:
    """Return the total from a list of counts."""
    return sum(counts)
