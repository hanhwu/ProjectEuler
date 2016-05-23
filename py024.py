# Lexicographic permutations
# Problem 24
# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time

def permutation_init(mix_these):
    return permutation_gen([], '', mix_these)
    

def permutation_gen(done_list, progress_string, remaining_members):
    # print 'debug: done_list, progress_string, remaining_members input to perumutation_gen ='
    # print done_list, progress_string, remaining_members
    if len(remaining_members) == 0:
        done_list.append(progress_string)
        return done_list
    else:
        for c in remaining_members:
            member_snapshot = remaining_members[:]
            member_snapshot.remove(c)
            progress_snapshot = progress_string + c
            done_list = permutation_gen(done_list, progress_snapshot, member_snapshot)
        return done_list
        

def solve024():
    start = time.time()
    permu_members_int = range(10) # problem set: range(10)
    permu_members_str = []
    for i in permu_members_int:
        permu_members_str.append(str(i))
        
    permu_results = permutation_init(permu_members_str)
    permu_results.sort()
    ans = permu_results[1000000-1]
    dur = time.time() - start
    print 'Answer', ans, 'found in', dur, 'seconds.'


solve024()
