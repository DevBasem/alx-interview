#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of operations needed
to result in exactly n H characters in a file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in a file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.
    """
    if n <= 1:
        return n

    # Initialize the result
    result = 0

    # Find prime factors of n
    for i in range(2, n + 1):
        while n % i == 0:
            result += i
            n //= i
        if n == 1:
            break

    return result
