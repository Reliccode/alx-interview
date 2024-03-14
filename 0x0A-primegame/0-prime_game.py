#!/usr/bin/python3
"""A game involving prime numbers between Maria and Ben"""


def isWinner(x, nums):
    """Determines the winner of the game based on prime numbers.

    Args:
        x (int): Number of rounds
        nums (list of int): List of numbers

    Returns:
        str or None: winner of game, None if inputs invalid
    """
    # Check for invalid inputs
    if x <= 0 or nums is None or x != len(nums):
        return None

    # Counters for Ben and Maria
    ben = 0
    maria = 0

    # Initialize a list with all elements set to 1
    a = [1 for _ in range(sorted(nums)[-1] + 1)]

    # Set the first two elements (0 and 1) to 0 as they are not primes
    a[0], a[1] = 0, 0

    # Generate a list of primes using Sieve of Eratosthenes algorithm
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Determine the winner based on the sum of primes up to the given number
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Compare Ben's and Maria's counts to determine the winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"

    # If counts are equal, return None
    return None


def rm_multiples(ls, x):
    """Remove multiples of a prime number.

    Args:
        ls (list): List of numbers
        x (int): Prime number

    Returns:
        None
    """
    for i in range(2, len(ls)):
        # Attempt to remove multiples of the prime number until IndexError or
        # ValueError
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
