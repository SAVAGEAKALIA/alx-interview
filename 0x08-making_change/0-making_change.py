#!/usr/bin/python3
"""
Module for making change using the minimum number of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total

    Args:
        coins (list): List of coin values available
        total (int): Target amount to make change for

    Returns:
        int: Minimum number of coins needed, -1 if total cannot be met
    """
    # Handle base cases
    if total <= 0:
        return 0

    # Sort coins in descending order for better performance
    coins = sorted(coins, reverse=True)

    # Initialize dp array with total + 1 (impossible value) as default
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build solution bottom-up
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                # Take minimum between current solution
                # and solution after using this coin
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return -1 if no solution found, otherwise return minimum coins needed
    return dp[total] if dp[total] != float('inf') else -1
