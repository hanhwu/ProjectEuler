# Lexicographic permutations
# Problem 24
# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time

def permutation_gen(already_done, add_these):
    for c in add_these:
        # continue here
    pass


def solve024():
    start = time.time()
    permu_members_int = range(10)
    permu_members_str = []
    for i in permu_members_int:
        permu_members_str.append(str(i))
        
    permu_results = permutation_gen('', permu_members_str)
    pass


solve024()
