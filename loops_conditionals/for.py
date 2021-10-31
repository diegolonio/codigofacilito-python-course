''' Iterable objects:
    - Lists
    - Tuples
    - Dictionaries
    - Strings '''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

dictionary = {'a': 1, 'b': 2, 'c': 3}
for key in dictionary:
    print(key)

values = ((10, 20), ['hola', 'como'], (True, False))
for value, subvalue in values:
    print(value, subvalue)