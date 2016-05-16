# Problem 15: Lattice Paths
# Starting in the top left corner of a 2×2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Solved by hand
# Generic solution:
#	For a grid n by m, find the combinations of n (rights) and m (downs)
#	combination = (n + m)! / (n! * m!)
#		Thought process:
#			Permutations for "(n+m) choose (n+m)" = (n + m)!, but:
#			(a)  We don't care what order the n's are, so divide by n!
#			(b)  We don't care what order the m's are, so divide by m!

import math

# Issue: math.factorial doesn't exist before 2.6
def factorial(x):
	assert type(x) is int, "factorial input type not INT"
	assert x >= 0, "factorial input less than zero"
	if x == 0:
		return 1
	else:
		return x * factorial(x - 1)


def solve15():
	n = 20
	m = 20
	ans = factorial(n + m) / (factorial(n) * factorial(m))
	print 'Program Answer =', ans


solve15()
	
