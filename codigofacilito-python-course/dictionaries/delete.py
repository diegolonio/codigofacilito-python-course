dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

# Delete an item
del dictionary['a']

# pop() function returns the deleted item
deleted = dictionary.pop('b')
print(deleted)

# Delete all the items in the dictionary
dictionary.clear()
print(dictionary)

# len() function returns the length of the dictionary
print(len(dictionary))