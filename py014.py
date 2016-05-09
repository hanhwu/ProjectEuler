# Problem 14
# Longest Collatz Sequence
#
# The following iterative sequence is defined for the set of positive integers:
# n -> n / 2  (n is even)
# n -> 3 * n + 1 (n is odd)
#
# Example:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# This sequence contains 10 terms.
#
# It has not been proven, but it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

import time

# collatzlength: Function to find the sequence length of starting number x.  Initializes sequence
# count at 1 and passes it on to the recursive portion of the program.
# Input: starting number <int> x
# Output: <int> n, length of Collatz sequence resulting from starting number x
def collatzlength(x):
	n = 1
	return collatznavigator(x, n)
	

# collatznavigator: Function that navigates to next Collatz after x, and keeps track of term count
# Input: <int> pair of collatz sequence member (x), and current sequence length (n)
# Recursive final output: <int> n, sequence length
def collatznavigator(x, n):
	if x == 1:
		return n
	elif x % 2 == 0:
		return collatznavigator(x / 2, n + 1)
	else:
		return collatznavigator(x * 3 + 1, n + 1)


# Function to solve problem 14 specifically
def solve14():
	start = time.time()
	ans = [1,1]
	for i in range(1,1000000):
		n = collatzlength(i)
		if n > ans[1]:
			ans = [i, n]
			print 'debug: ans = [i, n] =', ans
	dur = time.time() - start
	print 'Answer =', ans[0], 'found in', dur, 'seconds.'


solve14()
