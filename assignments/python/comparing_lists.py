def com_lists(l1, l2):
	if len(l1) not len(l2):
		print('not the same')
	else:
		for i in range(len(l1)):
			if l1[i] == l2[i]:
				continue
			else:
				print('not the same')
				break