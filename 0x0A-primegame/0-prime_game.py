#!/usr/bin/python3
"""
A prime numbers game
"""


def is_prime(num):
    """
    Check if num is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_sieve(limit):
    """
    Generate a list of prime nums upto a limit using Sieve of Eratosthenes
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return primes


def isWinner(x, nums):
    """
    Determine winner of each round of the prime game
    """
    winner_count = {"Maria": 0, "Ben": 0}

    # Iterate through each round
    for n in nums:
        primes = prime_sieve(n)
        maria_turn = True

        # Take turns removing prime nums
        while primes:
            if maria_turn:
                pick = max(primes)
                winner_count["Maria"] += 1
            else:
                pick = min(primes)
                winner_count["Ben"] += 1

            # Remove picked prime nums and its multiples
                primes = [p for p in primes if p % pick != 0]
                maria_turn = not maria_turn

    # Determine winner based on round outcomes
                if winner_count["Maria"] == winner_count["Ben"]:
                    return None
                return max(winner_count, key=winner_count.get)


# Test the function
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
