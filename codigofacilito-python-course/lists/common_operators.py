my_list = [8.17, 90, 1, 5, 44, 1.32]

# Sorting the list from greater to less
my_list.sort() # modifies the original list sorting it

sorted(my_list) # creates a sorted copy of the list

# Sorting the list from less to greater
my_list.sort(reverse=True)

# Get the less number in the list
less = min(my_list)

# Get the greater number in the list
greater = max(my_list)

# Get the cardinality of the list
cardinality = len(my_list)

# Know if an item is in the list
result = 8 in my_list

# Get the index of an item in the list
index = my_list.index(90)

# Get the frequency of an item in the list
frequency = my_list.count(1)