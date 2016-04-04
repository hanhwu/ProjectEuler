## A palindromic number reads the same both ways. The
## largest palindrome made from the product of two 2-digit
## numbers is 9009 = 91 × 99.
##
## Find the largest palindrome made from the product of
## two 3-digit numbers.

def ispalindrome(num):
    ## checks if a number is a palindrome
    return verdict


ans = 0
for i in range(100,1000,1):
    for j in range (i+1,1000,1):
        if ispalindrome(i*j) and i*j > ans:
            ans = i*j

print ans
