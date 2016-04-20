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
# F2. DoubleMaxT - Input: T <list> of triangle numbers; Output: New T <list> of triangle
#     numbers where max(T) is at least doubled.
#
# Main:
# 1. Generate and store triangle list, start from 0 (i.e. 0, 1, 3, 6, 10)
#    Such that T[n] = T[n-1] + n, and T[0] = 0
# 2. Check if the largest one has m divisors
# 3. If not enough, append T until new max(T) is at least double old max(T).  See F2.
#    Repeat until divisors exceed m, now we know the answer is in T somewhere.
#    Apply bisection search

