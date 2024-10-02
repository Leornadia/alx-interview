#!/usr/bin/python3

def is_prime(n):
    """Checks if a number is prime efficiently."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_game(n):
    """Determines the winner of a single round."""
    if n < 2:
        return "Ben"  # Maria loses immediately if no primes are available

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    
    count = sum(primes[2:])
    return "Maria" if count % 2 else "Ben"

def isWinner(x, nums):
    """Determines the overall winner over x rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":  # Explicitly check for "Ben"
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
