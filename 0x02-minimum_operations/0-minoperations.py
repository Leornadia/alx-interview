#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of operations
required to get 'n' characters using only "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations required to get 'n' characters
    using "Copy All" and "Paste" operations.

    Args:
        n: The target number of characters.

    Returns:
        The minimum number of operations required.
        If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            operations += 1
            n //= factor
        else:
            factor += 1

    return operations
