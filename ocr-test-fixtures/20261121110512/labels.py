def canonical_labels(labels: list[str]) -> list[str]:
    """Return sorted distinct labels, ignoring case and surrounding whitespace."""
    return sorted({label.strip().lower() for label in labels})
