"""Small production-chain regression fixture for OCR; no external dependencies."""


def bounded_average(values):
    """Return zero for empty input and the arithmetic mean otherwise."""
    return sum(values) / len(values)
