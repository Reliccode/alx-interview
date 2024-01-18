def minOperations(n):
    if n <= 0:
        return 0
    
    # Function to find prime factors of a number
    def prime_factors(num):
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
    
    # Find prime factors of n
    factors = prime_factors(n)
    
    # Return the sum of prime factors as the unconventional solution
    return sum(factors)

# Testing the unconventional solution
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
