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

    numbers = list(range(1, n + 1))
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        found_prime = False
        for i in range(len(numbers)):
            if numbers[i] != 0 and is_prime(numbers[i]): #Check if Number Exist and is prime
                found_prime = True
                prime_to_remove = numbers[i]
                numbers[i] = 0  #Remove the prime
                for j in range(i + 1, len(numbers)): #Remove multiples of the selected prime only
                    if numbers[j] != 0 and numbers[j] % prime_to_remove == 0:
                        numbers[j] = 0
                break

        if not found_prime:
            break

        turn += 1

    return "Maria" if turn % 2 == 0 else "Ben" #Maria starts

def isWinner(x, nums):
    """Determines the overall winner over x rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
