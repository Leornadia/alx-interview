#!/usr/bin/python3

def isWinner(x, nums):
  """
  Determines the winner of x rounds of the Prime Game based on optimal play.

  Args:
      x: Number of rounds to play.
      nums: List of consecutive integers (1 to n) for each round (n varies).

  Returns:
      str: Name of the player who wins the most rounds ("Maria" or "Ben").
      None: If the winner cannot be determined (a tie).
  """

  maria_wins, ben_wins = 0, 0
  for num_set in nums:
    # Check if starting number is even (guaranteed Ben win)
    if num_set[0] % 2 == 0:
      ben_wins += 1
      continue

    # Analyze remaining numbers for winnable state for Maria
    winnable = False
    for num in num_set:
      if is_prime(num):
        # Check if removing a prime leaves only even numbers (Ben wins)
        all_even = True
        for remaining in num_set:
          if remaining % 2 != 0:
            all_even = False
            break
        if not all_even:
          winnable = True
          break

    if winnable:
      maria_wins += 1
    else:
      ben_wins += 1

  # Determine winner based on round wins
  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None

def is_prime(n):
  """
  Checks if a number is prime (used for winnable state analysis).

  Args:
      n: The number to check for primality.

  Returns:
      bool: True if n is prime, False otherwise.
  """
  # Implement your prime checking logic here (e.g., trial division)
  # ...
