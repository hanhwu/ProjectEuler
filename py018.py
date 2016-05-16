# Maximum path sum I
# Find the path to traverse a triangle pile of numbers that yields the largest sum.
# Triangle number pile stored in 018ref.txt
# 
# Strategy:
# Add row 1 (1 number) to row 2 numbers
# Intelligently add row 2 numbers to row 3
#       For numbers that are not on the ends, there are two possible paths coming from
#       the previous row, choose the larger number since it is the better path.
# Proceed to next row, repeat the process of adding from previous row.

import time

def openfile(fn):
    wf = open(fn,'r')
    return wf


def texttointlist(wf):
    newlist = []
    for line in wf:
        newline = []
        newstr = ''
        for c in line:
            if c != '\n' and c != ' ':
                newstr = newstr + c
            else:
                newline.append(int(newstr))
                newstr = ''
                
        newlist.append(newline)
        
    print 'debug: newlist =', newlist
    return newlist


def solve018():
    start = time.time()
    filename = '018ref.txt'
    f = openfile(filename)
    numarray = texttointlist(f)
    for row in range(1,len(numarray)):
        print 'debug: row =', row
        for i in range(len(numarray[row])):
            if i == 0:
                numarray[row][i] += numarray[row-1][i]
            
            elif i == (len(numarray[row]) - 1):
                numarray[row][i] += numarray[row-1][i-1]
            
            else:
                numarray[row][i] += max(numarray[row-1][i-1], numarray[row-1][i])
    
    ans = max(numarray[-1])            
    dur = time.time() - start
    f.close()
    print 'Answer', ans, 'found in', dur, 'seconds.'
    # 1074 verified


solve018()
    
    
