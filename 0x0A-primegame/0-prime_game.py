#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """determines the winner of multiple rounds of the game"""
    def is_prime(num):
        """hecks if a given number num is prime or not."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_win(n):
        """determines whether player can win game with n as the starting nO"""
        if n == 1:
            return False
        elif n % 2 == 0:
            return True
        elif is_prime(n):
            return False
        else:
            return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
