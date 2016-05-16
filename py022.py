# Using names.txt (022ref.txt), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for
# each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
# What is the total of all the name scores in the file?

import time

def listbycomma(strfile):
    itemlist = []
    listmember = ''
    for c in namefile.read():
        if c == '"' or c == '\n':
            pass
        elif c == ',':
            itemlist.append(listmember)
            listmember = ''
        else:
            listmember += c
    
    return itemlist
    

def makedict():
    dtn = {}
    for i in range(26):
        dtn[chr(97 + i)] = i + 1
        print 'debug: ', char(97 + i), 'is', i + 1
    
    return dtn


def solve022():
    start = time.time()
    wf = open('022ref.txt','r')
    fnames = listbycomma(wf)
    fnames.sort()
    ltrnumdict = makedict()
    ans = 0
    idx = 1
    for str in fnames:
        nameint = 0
        for c in str:
            nameint += ltrnumdict[c]
        
        nameint *= idx
        ans += nameint
        idx += 1
    
    dur = time.time() - start
    print 'Answer', ans, 'found in', dur, 'seconds.'


solve022()
