#!/usr/bin/python3
"""Prime Game Module"""


def determine_winner(rounds, numbers):
    """
    Determines the game winner.

    Args:
        rounds (int): Number of rounds.
        numbers (list of int): List of numbers.

    Returns:
        str: Winner ("Ben" or "Maria"), or None.
    """
    if rounds <= 0 or numbers is None or rounds != len(numbers):
        return None

    ben_score, maria_score = 0, 0
    prime_flags = [1] * (max(numbers) + 1)
    prime_flags[0], prime_flags[1] = 0, 0

    for i in range(2, len(prime_flags)):
        remove_multiples(prime_flags, i)

    for n in numbers:
        if sum(prime_flags[:n + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None


def remove_multiples(prime_flags, prime):
    """
    Marks non-prime multiples.

    Args:
        prime_flags (list of int): Prime flags.
        prime (int): Current prime.
    """
    for i in range(2, len(prime_flags)):
        try:
            prime_flags[i * prime] = 0
        except (ValueError, IndexError):
            break
