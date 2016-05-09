# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import time

start = time.time()

f = open('013ref.txt','r')
line = f.readline()
largenumbersum = 0

while line != '':
	numstring = ''
	for i in line:
		if i != '\n':
			numstring += i
			
	largenumbersum += int(numstring)
	line = f.readline()
	
ans = str(largenumbersum)[0:10]
dur = time.time() - start
print 'Answer', ans, 'found in', dur, 'seconds.'

