"""Small fixture for the public Policy CI dispatch smoke test."""


def format_receipt_id(repository_id: int, pull_number: int) -> str:
    """Return a readable identifier for a pull request."""
    return f"{repository_id}:{pull_number}"
