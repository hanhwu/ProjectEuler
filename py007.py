# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10001st prime number?

import time


def find_nth_prime(n):
    """input: n-th prime to find (int)
    output: n-th prime (int)"""
    primes = [2]
    guess = 3
    while len(primes) < n:
        # keep adding primes to the end of the primes list
        # until desired n is reached
        isprime = True
        for i in primes:
            if guess % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(guess)
        guess += 1

    return primes[-1]


start = time.time()
x = 10001
print 'Found prime number', x, '(', find_nth_prime(10001), ') in', time.time(
) - start, 'seconds.'

# found 104743
