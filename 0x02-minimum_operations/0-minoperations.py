#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """calculates the fewest number of operations needed to result"""
    if n < 2:
        return 0

    operations = [0] * (n + 1)
    for i in range(2, n + 1):
        operations[i] = float('inf')
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + (i // j))

    return operations[n] if operations[n] != float('inf') else 0
