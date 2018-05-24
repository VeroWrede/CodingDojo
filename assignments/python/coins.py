from random import randint

def coinz(num):
	counter = 1
	heads = 0
	tails = 0
	log = 'head'
	while counter <= num:
		temp = randint(0,1)
		if temp == 0:
			log = 'head'
			heads += 1
		if temp	== 1:
			log = 'tail'
			tails += 1
		print 'throw # ',counter, '. It is ', log
		print heads, ' heads so far and ', tails, ' tails'
		counter += 1

	return heads, tails

coinz(10)