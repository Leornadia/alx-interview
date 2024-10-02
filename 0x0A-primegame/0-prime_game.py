#!/usr/bin/python3
"""Module to determine the winner of a prime game session."""

def sieve_of_eratosthenes(limit):
    """Returns a list where True means prime and False means not prime up to `limit`."""
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, limit + 1, i):
                primes[multiple] = False
    return primes

def count_primes(prime_list):
    """Returns a list of prime counts up to each index based on `prime_list`."""
    count_up_to = [0] * len(prime_list)
    prime_count = 0
    for i in range(1, len(prime_list)):
        if prime_list[i]:
            prime_count += 1
        count_up_to[i] = prime_count
    return count_up_to

def isWinner(rounds, nums):
    """Determines the winner after `rounds` rounds of the prime game."""
    if rounds < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_counts = count_primes(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Check the number of primes up to n
        prime_count = prime_counts[n]
        if prime_count % 2 == 1:
            maria_wins += 1  # Odd number of primes -> Maria wins
        else:
            ben_wins += 1  # Even number of primes -> Ben wins

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

