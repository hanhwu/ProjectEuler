# A perfect number is a number for which the sum of its proper divisors is 
# exactly equal to the number. For example, the sum of the proper divisors
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n 
# and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
# number that can be written as the sum of two abundant numbers is 24. By mathematical 
# analysis, it can be shown that all integers greater than 28123 can be written as 
# the sum of two abundant numbers. However, this upper limit cannot be reduced 
# any further by analysis even though it is known that the greatest number that
# cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time

def find_abundant_number(upper_limit):
    abuns = []
    for i in range(2, upper_limit):
        propdivs = 0
        for j in range(1, i):
            if i % j == 0:
                propdivs += j
        
        if propdivs > i
        abuns.append(i)
    
    return abuns


def solve023():
    start = time.time()
    abun_nums = find_abundant_number(28123 + 1)
    ans = 0
    for answer_guess in range(3,28123 + 1):
        failed_problem_criteria = False
        for a in abun_nums:
            for b in abun_nums:
                if answer_guess == a + b:
                    failed_problem_criteria = True
                elif a + b > answer_guess:
                    break
        
        if failed_problem_criteria == False:
            ans += answer_guess
    
    dur = time.time() - start
    print 'Answer', ans, 'found in', dur, 'seconds.'


solve023()
