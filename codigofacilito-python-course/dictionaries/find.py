dictionary = {'a': 1, 'b': 2, 'c': 3}

# Know if an item is in the dictionary
value = 'z' in dictionary

value = dictionary.get('x', 'The key doesn\'t exists')

"""
setdefault() returns the key's value if it exists,
if not, it creates a new key with the specified value
"""
value = dictionary.setdefault('d', 4)

print(dictionary)
print(value)