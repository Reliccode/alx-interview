#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """
    Calculates the fewest num of coins need to meet given amt total
    """
    # if the target total is less than 0, it cannot be met by any num of coins
    if total < 0:
        return 0
    # if target total is 0, no coins are needed
    if total == 0:
        return 0

    # an array to store min num of coins needed for each amt from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # iterate thru each coin denomination
    for coin in coins:
        # update dp[j] if using coin reduces num of coins need to make amt j
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # if dp[total] is still infinity, it means total caanot be met by any num
    # of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


# example usage
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
