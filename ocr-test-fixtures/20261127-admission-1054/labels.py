"""Deterministic label fixture for an OCR production smoke test."""


def normalize_label(label: str) -> str:
    """Remove surrounding whitespace and normalize case."""
    return label.strip().casefold()
