#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    # Find the prime factors of n
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1

    if n > 2:
        prime_factors.append(n)

    # Sum the prime factors, which gives the minimum number of operations
    return sum(prime_factors)
