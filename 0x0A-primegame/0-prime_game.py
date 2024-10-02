#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """
    Use Sieve of Eratosthenes to find all prime numbers up to n.
    Returns a list where the index is True if it is a prime number.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def count_prime_moves(n, primes):
    """
    Count how many prime numbers there are up to n, which translates into the number of moves.
    """
    return sum(primes[:n + 1])

def isWinner(x, nums):
    """
    Determines the winner of the game played in x rounds.
    
    Arguments:
    x -- number of rounds
    nums -- list containing the upper limit (n) for each round
    
    Returns:
    Name of the player who won the most rounds: "Maria" or "Ben".
    If the winner cannot be determined, return None.
    """
    if x <= 0 or not nums:
        return None
    
    # Precompute primes up to the maximum number in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    # Loop through each round
    for n in nums:
        prime_moves = count_prime_moves(n, primes)
        
        # If the number of prime moves is odd, Maria wins the round; if even, Ben wins
        if prime_moves % 2 == 1:
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

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Expected output: Ben

