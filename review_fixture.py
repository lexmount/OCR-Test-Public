"""Non-production fixture for validating OCR follow-up reviews."""


def average(values):
    """Return the arithmetic mean, or zero for an empty collection."""
    if not values:
        return 0
    return sum(values) / len(values)


def first_or_none(values):
    """Return the first value, or None if the collection is empty."""
    return values[0]
