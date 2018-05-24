from random import randint

def scores():
	score = randint(60, 100)
	return score

def grades(num):
	for n in range(num):
		score = scores()
		print(score)
		if 60 <= score <= 69:
			result = 'score: ', score, ' - grade: D'
		elif 70 <= score <= 79:
			result = 'score: ', score, ' - grade: C'
		elif 80 <= score <= 89:
			result = 'score: ', score, ' - grade: B'
		elif 90 <= score <= 100:
			result = 'score: ', score, ' - grade: A'
		else:
			result = 'Score out of range or some other problem'
		return result


print(grades(2))