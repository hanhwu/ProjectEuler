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
    for c in strfile.read():
        if c == '"':
            pass
        elif c == ',' or c == '\n':
            itemlist.append(listmember)
            listmember = ''
        else:
            listmember += c
    
    return itemlist
    

def makedict():
    dtn = {}
    for i in range(26):
        dtn[chr(65 + i)] = i + 1
        print 'debug: ', chr(65 + i), 'is', i + 1
    
    return dtn


def solve022():
    start = time.time()
    wf = open('022ref.txt','r')
    fnames = listbycomma(wf)
    fnames.sort()
    ltrnumdict = makedict()
    ans = 0
    idx = 0
    for aname in fnames:
        idx = idx + 1
        nameint = 0
        for c in aname:
            nameint = nameint + ltrnumdict[c]
        
        # print 'debug: aname, nameint, idx', aname, nameint, idx
        nameint = nameint * idx
        ans = ans + nameint

    dur = time.time() - start
    print 'Answer', ans, 'found in', dur, 'seconds.'


solve022()
