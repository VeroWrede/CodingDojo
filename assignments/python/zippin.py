name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def zipping(l1, l2):
	result = zip(l1,l2)
	return result

print zipping(name, favorite_animal)

