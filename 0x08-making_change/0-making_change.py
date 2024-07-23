#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The amount of money to make with coins.
    Returns:
        int: Fewest number of coins needed to meet the total.
             If the total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
