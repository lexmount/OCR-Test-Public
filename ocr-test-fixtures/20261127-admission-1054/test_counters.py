"""Smoke test for the counter fixture."""

from counters import total_counts


def test_total_counts() -> None:
    assert total_counts([2, 3, 5]) == 10
    assert total_counts([]) == 0
