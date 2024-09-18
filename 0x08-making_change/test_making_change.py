#!/usr/bin/python3
"""
Test script for the makeChange function
"""

from making_change import makeChange

def run_tests():
    test_cases = [
        ([1, 2, 25], 37, 7),
        ([1256, 54, 48, 16, 102], 1453, -1),
        ([1, 2, 5], 0, 0),
        ([1, 2, 5], -5, 0),
        ([2], 3, -1),
        ([1, 5, 10, 25], 10000, 400),
        ([1, 5, 10, 25], 100, 4),
        ([2, 5, 10, 20], 3, -1),
        ([1, 5, 10, 25], 30, 2),
        ([], 5, -1)
    ]

    for i, (coins, total, expected) in enumerate(test_cases, 1):
        result = makeChange(coins, total)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"  Input: coins = {coins}, total = {total}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    run_tests()
