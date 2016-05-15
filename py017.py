#   Problem 17:  Number Letter Counts
#   If all the numbers from 1 to 1000 (one thousand) inclusive 
#   were written out in words, how many letters would be used?
#   (Do not count hyphens and spaces)

#   Construct number-letter dictionary

import time

def makedict():
    dictx = {}
    dictx[1] = 3            #   one
    dictx[2] = 3            #   two
    dictx[3] = 5            #   three
    dictx[4] = 4            #   four
    dictx[5] = 4            #   five
    dictx[6] = 3            #   six
    dictx[7] = 5            #   seven
    dictx[8] = 5            #   eight
    dictx[9] = 4            #   nine
    dictx[10] = 3       #   ten
    dictx[11] = 6       #   eleven
    dictx[12] = 6       #   twelve
    dictx[13] = 8       #   thirteen
    dictx[14] = 8       #   fourteen
    dictx[15] = 7       #   fifteen
    dictx[16] = 7       #   sixteen
    dictx[17] = 9       #   seventeen
    dictx[18] = 8       #   eighteen
    dictx[19] = 8       #   nineteen
    dictx[20] = 6       #   twenty
    dictx[30] = 6       #   thirty
    dictx[40] = 5       #   forty
    dictx[50] = 5       #   fifty
    dictx[60] = 5       #   sixty
    dictx[70] = 7       #   seventy
    dictx[80] = 6       #   eighty
    dictx[90] = 6       #   ninety
    dictx[100] = 7      #   hundred
    dictx[1000] = 8     #   thousand
    dictx['&'] = 3      #   and
    return dictx

# lettercount:  counts the number of letters in n, using global dictionary letterdict
def lettercount(n,letterdict):
    # scope: 1-1000
    letters = 0
    assert n >=1
    assert n <=1000
    # parse 1000
    # print 'debug: n =', n
    if int(n // 1000) == 1:
        letters = letters + letterdict[1] + letterdict[1000]
    
    else:
        # parse hundreds + optional 'and'
        if int(n % 1000) >= 100:
            letters = letters + letterdict[int(n // 100)] + letterdict[100]
            if n % 100 > 0:
                letters = letters + letterdict['&']
        
        # parse tens and ones
        n = n % 100
        if n == 0:
                assert n == 0
        elif n <= 20:
            letters += letterdict[n]
        else:
            letters += letterdict[int(n // 10) * 10]
            n = n % 10
            if n > 0:
                letters += letterdict[n]

    return letters
            

def solve17():
    start = time.time()
    ans = 0
    dictx = makedict()  
    for i in range(1, 1000 + 1):
        ans += lettercount(i,dictx)
    
    dur = time.time() - start
    print 'Answer', ans, 'found in', dur, 'seconds.'
    # 21124 verified

solve17()
