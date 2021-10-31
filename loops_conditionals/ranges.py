for value in range(1, 20):
    print(value)

for value in range(-10, 11):
    print(value)

for number in range(2, 101, 2):
    print(number)

my_list = [1, 2, 3, 4, 5, 6]
for index in range(len(my_list)):
    print('Index:', index, 'Value:', my_list[index])

for index, value in enumerate(my_list):
    print('Index:', index, 'Value:', my_list[index])

for index, value in enumerate(my_list, 10):
    print('Index:', index, 'Value:', value)