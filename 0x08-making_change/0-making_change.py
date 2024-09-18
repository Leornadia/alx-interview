#!/usr/bin/python3
"""
This module contains the makeChange function which solves
the coin change problem.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount `total`.
    
    Args:
        coins (list of int): A list of coin denominations.
        total (int): The target amount to achieve with the coins.
    
    Returns:
        int: The minimum number of coins needed to meet `total`, or -1 if
        it's not possible to meet the `total` with the available coins.
    """
    # If the total is less than or equal to 0, no coins are needed
    if total <= 0:
        return 0

    # Initialize an array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make a total of 0

    # Iterate over each coin
    for coin in coins:
        # Update dp array for all amounts greater than or equal to the coin's value
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1

