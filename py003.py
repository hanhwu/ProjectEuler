## The prime factors of 13195 are 5, 7, 13 and 29.
##
## What is the largest prime factor of the number 600851475143 ?

import math

def makeprimelist(upperlimit):
    """Input int upperlimit; output list of primes up to upperlimit"""
    primelist = range(2,upperlimit,1)
    i = 0
    sifter = primelist[i]
    while sifter < int(math.sqrt(max(primelist)))+1:
        j = i+1
        while j < len(primelist):
            if primelist[j]%sifter == 0:
                del primelist[j]
            else:
                j += 1
        i += 1
        sifter = primelist[i]
        print sifter
    return primelist

x = 600851475143
ans = 1
primestocheck = makeprimelist(x)
for i in primestocheck:
    if x%i == 0:
        ans = i
print 'ans=',ans
