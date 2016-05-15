# Problem 16:  Power Digit Sum
#	What is the sum of the digits of 2**1000?

import time

def solve16():
	start = time.time()
	x = 2**1000
	ans = 0
	for c in str(x):
		ans += int(c)
	
	dur = time.time() - start
	print 'Answer', ans, 'found in', dur, 'seconds.'
	# 1366 confirmed

solve16()
	
