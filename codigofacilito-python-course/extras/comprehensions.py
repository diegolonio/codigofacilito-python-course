# Fill a list without comprehension
my_list = []
for x in range(0, 101):
    my_list.append(x)

# Fill a list with comprehension
structure = [ x for x in range(0, 101) ]

structure = [ 'Diego' for x in range(0, 101) ]

data = tuple( x for x in range(0, 101) )

pairs = [ x for x in range(0, 100) 
                    if x % 2 == 0 
                        if x < 50 ]

print(my_list)
print(structure)
print(data)
print(pairs)

# Generating a dictionary
dictionary  = { index:value for index, value 
                            in enumerate(structure) }

print(dictionary)