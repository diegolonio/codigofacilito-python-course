"""
Lists allow us to work as if they were matrices.
Despite of that, it's more recommended to work with
libraries like numpy that are specially developed
for this type of tasks
"""
# Declaring rows
row_one = [10, 20]
row_two = [30, 40]

# Defining a matrix as a column of rows
matrix = [row_one, row_two]

first_item = matrix[0][1]

print(first_item)