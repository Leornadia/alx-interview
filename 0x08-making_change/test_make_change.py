#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

def run_tests(test_file):
    with open(test_file, 'r') as file:
        lines = file.readlines()
    
    test_cases = []
    current_case = {}

    for line in lines:
        if "coins" in line:
            coins = eval(line.split('=')[1].strip())  # Convert the string list to a Python list
            current_case['coins'] = coins
        elif "total" in line:
            total = int(line.split('=')[1].strip())  # Extract total
            current_case['total'] = total
        elif "Expected Output" in line:
            expected = int(line.split('=')[1].strip())  # Extract expected output
            current_case['expected'] = expected
            test_cases.append(current_case)
            current_case = {}
    
    # Run each test case
    for i, case in enumerate(test_cases):
        coins = case['coins']
        total = case['total']
        expected = case['expected']
        result = makeChange(coins, total)

        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED (Expected {expected}, Got {result})")

if __name__ == "__main__":
    run_tests('0-making_change_test.txt')

