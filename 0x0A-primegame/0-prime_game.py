#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """
    Generate a list that marks prime numbers up to n using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def isWinner(x, nums):
    """
    Determines the winner of the prime game played in x rounds.
    
    Arguments:
    x -- number of rounds
    nums -- list containing the upper limit (n) for each round
    
    Returns:
    Name of the player who won the most rounds: "Maria" or "Ben".
    If the winner cannot be determined, return None.
    """
    if x <= 0 or not nums:
        return None

    # Find the maximum number in nums to optimize sieve computation
    max_n = max(nums)
    
    # Generate the prime numbers up to the maximum n in nums using Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        # If the number of primes up to n is odd, Maria wins; if even, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

