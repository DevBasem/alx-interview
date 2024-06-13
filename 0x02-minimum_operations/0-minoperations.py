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

    # Initialize the result with n itself because paste n times is an option
    result = n

    # Try all factors from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # If 'i' is a factor, recursively find the minimum operations
            # required for n/i characters and paste 'i' times
            result = min(result, i + minOperations(n // i))

    return result
