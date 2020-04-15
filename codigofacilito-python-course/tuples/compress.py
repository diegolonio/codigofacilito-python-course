my_tuple = (1, 2, 3, 4, 5, 6, 7)

one, two, three, four = my_tuple[0], my_tuple[1], my_tuple[2], my_tuple[3]

# It's the same as

# one, two, three, four = my_tuple

print(one)
print(two)
print(three)
print(four)

'''If cardinality of the tuple exceeds the number of variables
available we can put an asterisk before any of the variables
and the remaining values will be stored in that variable'''

one, two, *three, four = my_tuple

print(one)
print(two)
print(three)
print(four)

my_list = [10, 20, 30, 40]

another_tuple = (100, 200, 300, 400)

result = zip(my_tuple, my_list, another_tuple)

result = tuple(result)

print(result)

result = list(result)

print(result)