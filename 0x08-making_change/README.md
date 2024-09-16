# 0x08. Making Change

## Project Overview

This project focuses on the "Making Change" problem, a classic algorithmic challenge. The goal is to determine the fewest number of coins required to make up a given target amount, given a list of coin denominations. 

## File Description

* **0-making_change.py:** This file contains the Python function `makeChange(coins, total)`, which calculates the minimum number of coins needed to represent the `total` using the given `coins`. 

## How the Algorithm Works

The implemented solution uses a **greedy approach**:

1. **Sort Coins:** The provided coin denominations (`coins`) are first sorted in descending order. This prioritizes using larger coins first.
2. **Iterate and Subtract:** The algorithm iterates through the sorted coin list. For each coin denomination, it repeatedly subtracts the coin's value from the remaining total as long as the remaining total is greater than or equal to the coin value.  A counter keeps track of the number of coins used.
3. **Check for Success or Failure:** After attempting all coin denominations, the algorithm checks if the remaining total has been reduced to zero. If so, it means the target amount was successfully reached, and the number of coins used is returned. Otherwise, if the remaining total is not zero, it indicates that the target amount cannot be formed using the given coins, and -1 is returned.

## Example Usage

```python
from 0-making_change import makeChange

coins = [1, 2, 25]
total = 37

result = makeChange(coins, total)

print(f"Minimum coins required: {result}")  # Output: 7
