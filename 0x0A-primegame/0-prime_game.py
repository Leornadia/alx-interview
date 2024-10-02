#!/usr/bin/python3

def is_prime(n):
    """Efficiently checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_game(n):
    """Determines the winner of a single round."""
    if n < 2:
        return "Ben"

    numbers = list(range(1, n + 1))  # List of numbers in the game
    turns = 0

    while True:
        found_prime = False
        for i in range(len(numbers)):
            if numbers[i] > 0 and is_prime(numbers[i]):  #Check If Number Exist and is prime
                found_prime = True
                p = numbers[i]
                for j in range(len(numbers)):
                    if numbers[j] % p == 0:
                        numbers[j] = 0  # "Remove" multiples of the prime
                break  # Move to next player's turn after removing prime

        if not found_prime:
            break # No primes left, game ends

        turns += 1

    return "Maria" if turns % 2 == 1 else "Ben"  # Maria starts


def isWinner(x, nums):
    """Determines the overall winner over x rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
