#!/usr/bin/python3

def is_prime(num):
    """Efficiently checks if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_game(n):
    """Determines the winner of a single round of the Prime Game."""
    if n < 2:
        return "Ben"  # No prime numbers to choose, Ben wins

    primes = [num for num in range(2, n + 1) if is_prime(num)]
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

    return "Maria" if turn % 2 != 0 else "Ben"  # Maria goes first


def isWinner(x, nums):
    """Determines the overall winner of x rounds of the Prime Game."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:  # Handles Ben wins and other cases
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
