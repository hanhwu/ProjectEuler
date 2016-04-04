## A palindromic number reads the same both ways. The
## largest palindrome made from the product of two 2-digit
## numbers is 9009 = 91 × 99.
##
## Find the largest palindrome made from the product of
## two 3-digit numbers.

def ispalindrome(numstr):
    """input str; returns bool"""
    if len(numstr)>2 and numstr[0]==numstr[-1]:
        return ispalindrome(numstr[1:-1])
    elif len(numstr) == 2 and numstr[0]==numstr[1]:
        return True
    elif len(numstr) == 1:
        return True
    else:
        return False

## setup for problem 004
    
ans = 0
for i in range(100,1000,1):
    for j in range (i+1,1000,1):
        if ispalindrome(str(i*j)) and i*j > ans:
            ans = i*j
print ans
