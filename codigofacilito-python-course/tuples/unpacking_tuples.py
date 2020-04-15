my_tuple = (10, 20, 30, 40, 50)

# Working with indices

first = my_tuple[0]
second = my_tuple[1]
last = my_tuple[-1]

first, second, last = my_tuple[0], my_tuple[1], my_tuple[-1]

# Working without indices

first, second, _, _, last = my_tuple

print(first)
print(second)
print(last)

first, second, *_, last = my_tuple

print(first)
print(second)
print(last)