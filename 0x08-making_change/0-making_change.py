#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given amount total.

    Args:
    - coins: list of ints representing values of coins in possession.
    - total: An integer representing the target total amount.

    Returns:
    - fewest num of coins needed to meet total.
      If total cannot be met by any number of coins you have, return -1.
    """
    # If the target total is less than 0, it cannot be met by any number of
    # coins
    if total < 0:
        return 0
    # If the target total is 0, no coins are needed
    if total == 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each
    # amount from 1 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update dp[j] if using coin reduces the number of coins needed to make
        # amount j
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met by any
    # number of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


# Example usage
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output should be 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output should be -1
