# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time

def find_triplet(n):
  """Returns A*B*C for A**2 + B**2 = C**2, and A+B+C=n"""
  ## range of guesses:
  ## a:    1    to  n//3
  ## b:    a+1  to  a+1 + (n-a)//2
  ## c:    n-a-b
  ## check that a<b and b<c, there are edge cases
  ans = None
  for a in range(1, n // 3 + 1):
    for b in range(a + 1, a + 1 + (n - a) // 2 + 1):
      c = n - a - b
      if a < b and b < c and a**2 + b**2 == c**2:
        ans = a * b * c
  return ans
  
start = time.time()
n = 1000
ans = find_triplet(n)
solve_time = time.time() - start
print 'Answer', ans, 'found in', int(solve_time)+1, 'seconds'
