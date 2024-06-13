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
        return 0

    # Function to calculate prime factors of a number
    def prime_factors(num):
        factors = []
        while num % 2 == 0:
            factors.append(2)
            num //= 2
        for i in range(3, int(num**0.5) + 1, 2):
            while num % i == 0:
                factors.append(i)
                num //= i
        if num > 2:
            factors.append(num)
        return len(factors)

    # Get prime factors count of n
    return prime_factors(n)
