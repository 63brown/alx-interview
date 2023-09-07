#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """determines winner"""
    def is_prime(num):
        """picks a prime number"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_win(n):
        """determines win"""
        if n == 1 or (n % 2 == 0 and n != 2):
            # Ben wins when n is 1 or an even number greater than 2
            return "Ben"
        else:
            # Maria wins if Maria starts with an odd prime number
            return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n) == "Ben":
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
