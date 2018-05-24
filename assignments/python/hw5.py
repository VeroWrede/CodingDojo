def check_type(some_arr):
	#making groups
	strs = ""
	bls = []
	ints = 0
	dicts = []
	track = [0, 0, 0, 0]

	#check types and append/add item to corresponding group
	for item in some_arr:
		if type(item) == str:
			strs += item
			track[0] = 1
		elif type(item) == int or type(item) == float:
			ints += item
			track[1] = 5
		elif type(item) == bool:
			bls.append(item)
			track[2] = 10
		elif type(item) == dict:
			dicts.append(item)
			track[3] = -2
		else:
			print('type not defined for ',item)

	#checking outcome and printing result
	if sum(track) == 1:
		print('only strings')
		a = ' '
		print(a.join(some_arr))
	elif sum(track) == 5:
		print('only ints')
		print('sum: ', sum(some_arr))
	elif sum(track) == 10:
		print('only bools')
		print(some_arr)
	elif sum(track) == -2:
		print('only dicts')
		print(some_arr)
	else:
		print('mixed arr')
		print('strings: ', strs) 
		print('numbers: ',ints)
		print('booleans: ', bools)
		print('dictionaries: ', dicts)

