# Counting Sundays
# 1900/1/1 was a Monday
# How many Sundays fell on the first of the month in the 20th Century? (1901/1/1 to 2000/12/31)
# Leap year conditions:
#   Year divisible by 4
#   Year divisible by 400
#   NOT Year divisible by 100, but not 400 
#   (i.e. 2000 leaps, 1900 doesn't)

from datetime import datetime, date, timedelta

def solve019():
    startdate = date(1901, 1, 1)
    enddate = date(2000, 12, 31)
    testdate = startdate
    inc = timedelta(days = 1)
    ans = 0
    while testdate <= enddate:
        if testdate.day == 1 and testdate.weekday() == 6:
            ans += 1
            # print 'debug: sunday found on testdate =', testdate
        
        testdate += inc
    
    print "Answer", ans, "found."


solve019()
