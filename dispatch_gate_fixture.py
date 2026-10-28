"""Disposable fixture for admission checks; no production behavior."""


def average_or_zero(values):
    items = tuple(values)
    return sum(items) / len(items) if items else 0
