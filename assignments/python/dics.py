me = {
	'name': 'Vero',
	'age': 25,
	'pet': 'Mina',
	'job': 'SE',
	'languages': ['German', 'French', 'Spanish', 'English']
}

# print me.items()

def dict_stuff(dct):
	for key, item in dct.items():
		print 'my ', key, ' is ', item 
		
dict_stuff(me)
