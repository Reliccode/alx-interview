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
      If total cannot be met by any number of coins you have
    """
    # If coins is empty or None, return -1 indicating invalid input
    if not coins or coins is None:
        return -1
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    change = 0  # Initialize the variable to count the number of coins used
    coins = sorted(coins)[::-1]  # Sort coins in descending order
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1  # Increment the count of coins used
        if total == 0:  # If total becomes 0, return the count of coins used
            return change
    return -1  # If total cannot be met by any number of coins, return -1
