## Smallest multiple
## 2520 is the smallest number that can be divided by
## each of the numbers from 1 to 10 without any remainder.
##
## What is the smallest positive number that is evenly
## divisible by all of the numbers from 1 to 20?

# Function to find smallest positive number that is evenly
# divisible by numbers from a to b
def small_mult(a,b):
    """in: int a,b; out: int"""
##    ans = 1
##    solution_unknown = True
##    while solution_unknown:
##        for i in range(a,b+1):
##            if ans%i != 0:
##                ans += 1
##                break
##            elif i == b:
##                solution_unknown = False
##                break
##    return ans

    divisors = range(a,b+1)
    common_primes = []
    while len(divisors) > 0:
# remove 1s in divisors
        i = len(divisors)-1
        while i >= 0:
            if divisors[i] == 0:
                del divisors[i]
            i -= 1
# check for divisors mod 2 and iterate up
# when found, divide, replace, restart, and add to common_primes list
        j = 2
            
            
            
            


# Problem setup (1,10 -> 2520 verified)
# Inefficient method found 1,20 -> 232792560
x = 1
y = 20
print 'Running!'
print 'Ans = ',small_mult(x,y)
