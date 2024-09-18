#!/usr/bin/python3

def makeChange(coins, total):
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

# Example usage:
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

