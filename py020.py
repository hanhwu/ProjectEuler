# Factorial Digit Sum
# Find digit sum of 100!

import time

def factorial(n):
    assert type(n) is int
    if n == 0:
        return 1
        
    else:
        return n * factorial(n - 1)


def sumdigits(n):
    cn = 0
    for c in str(n):
        cn += int(c)
        
    return cn


def solve020():
    ans = sumdigits(factorial(100))
    print 'Answer', ans, 'found.'


solve020()
