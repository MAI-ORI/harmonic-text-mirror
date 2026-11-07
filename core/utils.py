def digital_root(n):
    """Calculate the digital root of an integer using 1-9 modular reduction."""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9
