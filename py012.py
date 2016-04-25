# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# Functions:
# F1. Divisors - Input: n <int>; Output: divs <int> number of divisors of n

import math
import time

def divisors(n):
    print 'debug: divisors called for', n
    divs = 0
    if math.sqrt(n) % 1 == 0:
        divs += 1
        
    for i in range(1, int(math.sqrt(n) // 1)):
        if n % i == 0:
            divs += 2
            print i, n/i
    return divs
    
# main
start = time.time()
trinum = 1
n = 2
m = 501     # m = number of divisors we're looking for

while divisors(trinum) < m:
    trinum += n
    n += 1

ans = trinum
dur = time.time() - start
print 'ans', ans, 'found in', dur, 'seconds.'
