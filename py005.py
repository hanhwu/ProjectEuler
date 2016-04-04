## Smallest multiple
## 2520 is the smallest number that can be divided by
## each of the numbers from 1 to 10 without any remainder.
##
## What is the smallest positive number that is evenly
## divisible by all of the numbers from 1 to 20?


# Function to find smallest positive number that is evenly
# divisible by numbers from a to b
def small_mult(a, b):
    """in: int a,b; out: int"""
    divisors = range(a, b + 1)
    common_primes = []
    while len(divisors) > 0:
        # check for even divisors from 2 and iterate up
        # when found, update divisors, restart from 2, and add to common_primes list
        common_found = False
        for j in range(2, max(divisors) + 1):
            for i in range(len(divisors)):
                if divisors[i] % j == 0:
                    divisors[i] = divisors[i] / j
                    common_found = True
            if common_found:
                common_primes.append(j)
                break
        # remove 1s in divisors
        i = len(divisors) - 1
        while i >= 0:
            if divisors[i] == 1:
                del divisors[i]
            i -= 1

    result = 1
    for i in common_primes:
        result = result * i
    return result

    # Problem setup (1,10 -> 2520 verified)
    # Inefficient method found 1,20 -> 232792560


x = 1
y = 20
print 'Running!'
print 'Ans = ', small_mult(x, y)
print 'Done!'
