## The sum of the squares of the first ten natural numbers is,
## 1^2 + 2^2 + ... + 10^2 = 385
## 
## The square of the sum of the first ten natural numbers is,
## (1 + 2 + ... + 10)^2 = 3025
##
## Hence the difference between the sum of the squares of the
## first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
## 
## Find the difference between the sum of the squares of the
## first one hundred natural numbers and the square of the sum.

def sum_sq_diff(a):
    """input a (int); output sum-sq-diff of first 'a' natural numbers (int)"""
    ans = sum(range(a+1))**2
    for i in range(1,a+1):
        ans = ans - i**2
    return ans

print sum_sq_diff(100)
