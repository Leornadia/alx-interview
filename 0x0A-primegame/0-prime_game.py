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
    """Determines the winner of a single round of the Prime Game."""
    if n < 2:
        return "Ben"  # No primes available, Maria loses immediately

    primes = [number for number in range(2, n + 1) if is_prime(number)]
    numbers = list(range(1, n + 1))
    turn = 0

    while True:
        found_move = False
        for p in primes:
            if p in numbers:
                for num in list(numbers):  # Iterate over copy to modify original
                    if num % p == 0:
                        numbers.remove(num)
                found_move = True
                break

        if not found_move:
            break

        turn += 1

    if turn == 0: # Case n=1, 0, no primes no moves, Ben wins by default
        return "Ben"

    if turn % 2 == 1:
        return "Maria"
    else:
        return "Ben"


def isWinner(x, nums):
    """
    Determines the overall winner of x rounds of the Prime Game.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":  # Explicitly check for "Ben" to handle potential None
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
