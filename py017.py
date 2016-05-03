#	Problem 17:  Number Letter Counts
#	If all the numbers from 1 to 1000 (one thousand) inclusive 
#	were written out in words, how many letters would be used?
#	(Do not count hyphens and spaces)

#	Construct number-letter dictionary

import time

def makedict():
	dict = {}
	dict[1] = 3			#	one
	dict[2] = 3			#	two
	dict[3] = 5			#	three
	dict[4] = 4			#	four
	dict[5] = 4			#	five
	dict[6] = 3			#	six
	dict[7] = 5			#	seven
	dict[8] = 5			#	eight
	dict[9] = 4			#	nine
	dict[10] = 3		#	ten
	dict[11] = 6		#	eleven
	dict[12] = 6		#	twelve
	dict[13] = 8		#	thirteen
	dict[14] = 8		#	fourteen
	dict[15] = 7		#	fifteen
	dict[16] = 7		#	sixteen
	dict[17] = 9		#	seventeen
	dict[18] = 8		#	eighteen
	dict[19] = 8		#	nineteen
	dict[20] = 6		#	twenty
	dict[30] = 6		#	thirty
	dict[40] = 5		#	forty
	dict[50] = 5		#	fifty
	dict[60] = 5		#	sixty
	dict[70] = 7		#	seventy
	dict[80] = 6		#	eighty
	dict[90] = 6		#	ninety
	dict[100] = 7		#	hundred
	dict[1000] = 8		#	thousand
	dict['&'] = 3		#	and
	return dict

# lettercount:  counts the number of letters in n, using global dictionary letterdict
def lettercount(n):
	# scope: 1-1000
	letters = 0
	if n > 1000 or n < 1:
		print 'Debug: n out of dictionary range, n =', n
		break
		
	else:
		# parse 1000
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
			if n <= 20:
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
	letterdict = makedict()	
	for i in range(1, 1000 + 1):
		ans += lettercount(i)
	
	dur = time.time() - start
	print 'Answer', ans, 'found in', dur, 'seconds.'


solve17()
