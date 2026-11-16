"""Small, side-effect-free fixture for OCR deployment verification."""


def task_batches(task_ids: list[str], batch_size: int) -> list[list[str]]:
    """Return ordered batches without modifying the input list."""
    if type(batch_size) is not int:
        raise TypeError("batch_size must be an integer")
    if batch_size < 1:
        raise ValueError("batch_size must be positive")
    return [task_ids[start:start + batch_size]
            for start in range(0, len(task_ids), batch_size)]
