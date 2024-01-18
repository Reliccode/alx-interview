#!/usr/bin/env python3
'''
Min operations
'''


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file.

    Parameters:
    - n (int): The target number of H characters.

    Returns:
    - int: The minimum number of operations needed.
    If n is impossible to achieve, returns 0.
    """

    if n <= 0:
        return 0

    def prime_factors(num):
        """
        Finds the prime factors of a given number.

        Parameters:
        - num (int): The number for which prime factors are to be found.

        Returns:
        - list: List of prime factors.
        """
        factors = []
        divisor = 2
        while divisor * divisor <= num:
            while (num % divisor) == 0:
                factors.append(divisor)
                num //= divisor
            divisor += 1
        if num > 1:
            factors.append(num)
        return factors

    factors = prime_factors(n)
    return sum(factors)


# Testing the unconventional solution
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
