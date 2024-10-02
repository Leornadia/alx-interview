#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    
    Args:
        x: The number of rounds.
        nums: List of integers, where each integer represents the range [1, n] for that round.
        
    Returns:
        'Maria' if Maria wins more rounds, 'Ben' if Ben wins more rounds, or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    # Find the maximum number in nums to generate primes up to that limit
    n = max(nums)

    # Sieve of Eratosthenes to find all prime numbers up to n
    primes = [True] * (n + 1)  # Initialize the sieve list with True
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Count wins for Maria and Ben
    marias_wins = 0
    bens_wins = 0

    # Determine the winner for each round
    for num in nums:
        if prime_count[num] % 2 == 1:
            marias_wins += 1
        else:
            bens_wins += 1

    # Determine the overall winner
    if marias_wins > bens_wins:
        return 'Maria'
    elif bens_wins > marias_wins:
        return 'Ben'
    else:
        return None

