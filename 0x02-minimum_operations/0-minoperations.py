#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of
operations needed to result in exactly n H characters
in a file.
"""


def minOperations(n):
    """
    Computes the minimum number of operations needed for
    the Copy All and Paste task.

    Args:
        n: The desired number of H characters.

    Returns:
        The sum of the operations.
    """
    if n < 2:
        return 0
    operations = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                operations.append(i)
    return sum(operations)
