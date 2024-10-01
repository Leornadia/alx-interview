#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    
    Args:
    x (int): The number of rounds.
    nums (list): An array of n for each round.
    
    Returns:
    str: Name of the player that won the most rounds.
         If the winner cannot be determined, returns None.
    """
    def sieve_of_eratosthenes(n):
        """Generate primes up to n using Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    def play_round(n):
        """Simulate a round of the game."""
        primes = sieve_of_eratosthenes(n)
        return len(primes) % 2 == 1  # Maria wins if odd number of primes

    if not nums or x <= 0:
        return None

    maria_wins = sum(play_round(n) for n in nums[:x])
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
