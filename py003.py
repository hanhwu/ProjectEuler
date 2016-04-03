## The prime factors of 13195 are 5, 7, 13 and 29.
##
## What is the largest prime factor of the number 600851475143 ?

def FindLargestPrimeFactor(x):
    x = 600851475143
    ans = 1
    i = 2
    while i <= x:
        if x%i == 0:
            x = x / i
            ans = i
            ## progress checkprint: print 'x=',x,' ans=',ans
            i = 2
        i += 1

print FindLargestPrimeFactor(600851475143)

                
            







    
