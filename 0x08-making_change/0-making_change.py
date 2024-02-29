#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The target amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin_value in coins:
        # Update min_coins
        for amount in range(coin_value, total + 1):
            min_coins[amount] = min(min_coins[amount],
                                    min_coins[amount - coin_value] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
