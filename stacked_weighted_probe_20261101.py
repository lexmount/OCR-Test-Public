"""Dependent layer for the isolated stacked PR review fixture."""

from stacked_probe_20261101 import average


def weighted_average(values, weights=None):
    """Return the weighted mean, or 0 when the total weight is zero."""
    if weights is None:
        return average(values)
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    return sum(value * weight for value, weight in zip(values, weights)) / sum(weights)
