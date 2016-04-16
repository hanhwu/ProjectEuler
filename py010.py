# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
import time

def find_primes(n):
    """input: n as search limit
    output: list of primes"""
    primes = [2]
    guess = 3
    while primes[-1] < n:
        # keep adding primes to the end of the primes list
        # until desired n is reached
        isprime = True
        for i in primes:
            if guess % i == 0:
                isprime = False
                break
            elif i > math.sqrt(guess):
                break
        if isprime:
            primes.append(guess)
        guess += 1

    return primes[0:-1]  # because last one exceeds n

n = 2000000
start = time.time()
plist = find_primes(n)
solve_time = time.time() - start
ans = sum(plist)
print 'Answer',ans,'found in',solve_time,'seconds.'
