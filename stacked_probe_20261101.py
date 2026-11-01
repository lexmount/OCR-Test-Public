"""Isolated stacked PR review fixture; not intended for production use."""


def average(values):
    """Return the arithmetic mean; reject an empty input."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
