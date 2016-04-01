## If we list all the natural numbers below 10 that are
## multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
## these multiples is 23.
##
## Find the sum of all the multiples of 3 or 5 below 1000.

def Find_Sum_of_Multiples(m1,m2,upperlimit):
    ans = 0
    for _ in range(1,upperlimit):
        if _%m1 == 0 or _%m2 == 0:
            ans += _
    return ans

print Find_Sum_of_Multiples(3,5,1000)

