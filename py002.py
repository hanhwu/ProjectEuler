## Each new term in the Fibonacci sequence is generated 
## by adding the previous two terms. By starting with 1 
## and 2, the first 10 terms will be:
##
## 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
##
## By considering the terms in the Fibonacci sequence whose 
## values do not exceed four million, find the sum of the
## even-valued terms.

def FindEvenFibSum( upperlimit ):
    x1 = 1
    x2 = 2
    x3 = x1 + x2
    ans = 2
    while x3 < upperlimit:
        if x3%2 == 0:
            ans += x3
        x1 = x2
        x2 = x3
        x3 = x1 + x2
    return ans

print FindEvenFibSum(4000000)



