"""Small offline fixture for the production worktree acceptance review."""


def batch_ranges(total: int, batch_size: int = 8) -> list[tuple[int, int]]:
    """Return non-overlapping half-open ranges covering exactly total items."""
    if type(total) is not int or total < 0:
        raise ValueError("total must be a non-negative integer")
    if type(batch_size) is not int or batch_size < 1:
        raise ValueError("batch_size must be a positive integer")
    return [
        (start, min(start + batch_size, total))
        for start in range(0, total, batch_size)
    ]
