# Amicable Numbers
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
#
# If d(a) == b and d(b) == a, where a != b, then a and b
# are an amicable pair and each of a and b are called amicable numbers.
# Ex:
# The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
# so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import time

def propdivsum(n):
    assert type(n) is int
    dsum = 0
    for i in range(1, n):
        if n % i == 0:
            dsum += i
    
    return dsum


def solve021():
    start = time.time()
    ans = 0
    ubound = 10000
    for i in range(2, ubound):
        a = propdivsum(i)
        b = propdivsum(a)
        if i == b and i != a:
            if a >= ubound:
                print 'debug:', a, '> ubound, pairs', i, 'and', a, 'not recorded.'
            else:
                print 'debug: amicable pair (', i, ',', a, ') added.'
                ans = ans + i + a
    
    ans = ans / 2       # since everything got counted twice
    dur = time.time() - start
    print 'Answer', ans, 'found in', dur, 'seconds.'


solve021()
