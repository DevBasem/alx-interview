#!/usr/bin/python3
"""Module for Prime Game"""


def determine_winner(rounds, numbers):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        rounds (int): The number of rounds.
        numbers (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Check for invalid input
    if rounds <= 0 or numbers is None:
        return None
    if rounds != len(numbers):
        return None

    # Initialize scores for Ben and Maria
    ben_score = 0
    maria_score = 0

    # Create a list 'prime_flags' with all elements initialized to 1
    prime_flags = [1 for _ in range(max(numbers) + 1)]

    # Mark 0 and 1 as non-prime
    prime_flags[0], prime_flags[1] = 0, 0

    # Use Sieve of Eratosthenes algorithm to generate array of prime numbers
    for i in range(2, len(prime_flags)):
        remove_multiples(prime_flags, i)

    # Play each round of the game
    for n in numbers:
        # If the sum of prime numbers in the set is even, Ben wins
        if sum(prime_flags[:n + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    # Determine the winner of the game
    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None


def remove_multiples(prime_flags, prime):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        prime_flags (list of int): An array representing possible prime numbers.
        prime (int): The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    # This loop marks multiples of a prime number as non-prime by setting
    # their corresponding value to 0 in the prime_flags list.
    for i in range(2, len(prime_flags)):
        try:
            prime_flags[i * prime] = 0
        except (ValueError, IndexError):
            break
