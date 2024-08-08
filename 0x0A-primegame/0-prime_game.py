#!/usr/bin/python3
"""Module defining the isWinner function."""


def isWinner(round_count, nums):
    """Determines the winner of the prime game."""
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        current_numbers = list(range(1, num + 1))
        prime_numbers = find_primes_in_range(1, num)

        if not prime_numbers:
            ben_wins += 1
            continue

        maria_turn = True

        while True:
            if not prime_numbers:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            smallest_prime = prime_numbers.pop(0)
            current_numbers.remove(smallest_prime)
            current_numbers = [
                n
                for n in current_numbers
                if n % smallest_prime != 0
            ]

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Winner: Maria"

    if ben_wins > maria_wins:
        return "Winner: Ben"

    return None


def is_prime(n):
    """Returns True if n is a prime number, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    return [n for n in range(start, end + 1) if is_prime(n)]
