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

def solve15():
	n = 20
	m = 20
	ans = math.factorial(n + m) / (math.factorial(n) * math.factorial(m))
	print 'Program Answer =', ans, ', should be 137846528820 per hand-calc.'
	# should be 137846528820, run and check

solve15()
	
