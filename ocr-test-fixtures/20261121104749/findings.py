def total_with_fee(subtotal_cents: int, fee_cents: int) -> int:
    """Return the subtotal plus the fee, in cents."""
    return subtotal_cents - fee_cents
