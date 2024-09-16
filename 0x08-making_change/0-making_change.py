#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins: A list of coin denominations.
        total: The target amount.

    Returns:
        The fewest number of coins needed, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to try larger denominations first (greedy)
    coins.sort(reverse=True)

    num_coins = 0
    remaining_total = total

    for coin in coins:
        while remaining_total >= coin:
            remaining_total -= coin
            num_coins += 1

    if remaining_total == 0:
        return num_coins
    else:
        return -1 
