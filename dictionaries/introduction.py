# Dictionaries can be defined in two ways

dictionary = {}

dictionary = dict(key='value', another_key='another value')

# ==================================================================
# Dictionaries are similar to associative arrays on php

dictionary = {'total': 55}

dictionary = {'total': 55, 'discount': True, 'subtotal': 15}

dictionary = {'total': 55, 10: 'python course', (1, 2, 3): True}

print(dictionary)
# ==================================================================
# Classes as keys
user = {
	'name': 'Diego Armando Apolonio Villegas',
	'age': 18,
	'course': 'Python 3 Course',
	'skills': {
		'programming': True,
		'data_bases': False
	},
	'medals': ['basic', 'intermediate']
}
# ==================================================================
# Creating an emty dictionary
dictionary = dict()

# Add a new key with its value
dictionary['user'] = 'Diego Armando Apolonio Villegas'

# Update value by key
dictionary['user'] = 'Erick Berrueco Izurieta'

# Get value by key
print(dictionary['user'])
# ==================================================================
dictionary = {'Diego': 1, 'Jared': 2, 'Yafit': 3, 'Fernanda': 4, 'May': 5}

# Get all the dictionary's keys
print(dictionary.keys())

# Get all the dictionary's values
print(dictionary.values())

# Iterate the dictionary to show each key with its value
for key, value in dictionary.items() :
	print(key, value)
# ==================================================================
user = {
	'name': 'Diego Apolonio',
	'age': 18,
	'job': 'student'
}

"""
get() function allow us to get the key of the specified value in the first
parameter, if the key doesn't exists, it returns the value specified in the
second parameter
"""
califications = user.get('califications', [])

if califications :
	for calification in califications :
		print(calification)

# Comprehension
users = ['Diego', 'Jared', 'Yafit']

dictionary = {user:position + 1
			for position, user in enumerate(users)}

print(dictionary)