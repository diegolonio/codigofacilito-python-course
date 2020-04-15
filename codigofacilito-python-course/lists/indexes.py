courses = ['python', 'django', 'flask', 'c', 'c++', 'c#', 'java', 'php']

course = courses[-2]

# Get a sublist
# list[ from index : how many ]
sub = courses[0:3]

# Get the number of items indicated from the start
sub = courses[:3]

# Get the list items from the index indicated to the end
sub = courses[3:]

# Get all the elements exactly like they stand
sub = courses[:]

# Get the number of items indicated from the start each n skips
sub = courses[1:4:2]

# Get the reversed list
sub = courses[::-1]

print(sub)