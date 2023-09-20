#!/usr/bin/python3
"""
0-making_change.py
"""

def makeChange(coins, total):
    """ determines the fewest number of coins needed to meet a given total amount"""
    dp = [float('inf')] * (total + 1)
    
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    
    return dp[total]

if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
