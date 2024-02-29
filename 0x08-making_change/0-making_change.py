#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total.

    Args:
    - coins: A list of integers representing the values of the coins
    - total: An integer representing the target total amount.

    Returns:
    - The fewest number of coins needed to meet the total.
      If total cannot be met by any number of coins you have, return -1.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update dp[j] if using coin reduces the number of coins
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # If dp[total] is still infinity, means total cannot be met by any num of
    # coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
