"""Review-only fixture: intentionally contains a boundary bug; not production code."""


def average(values):
    """Return the arithmetic mean, or zero for an empty collection."""
    return sum(values) / len(values)
