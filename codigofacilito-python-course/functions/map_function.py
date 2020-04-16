'''In Python, map function allow us to apply a function
in the items of an object (lists, tuples, etc...).

Syntaxis: map(<function>, <iterable object>)

map() returns an object that we can later convert into a 
list or a tuple'''
def square(number):
    return number * number
my_list = [1, 2, 3, 4, 5]
result = map(square, my_list)
resulting_list = list(result)
print(my_list)
print(resulting_list)

'''It's possible to use map() function as a lambda function'''
result = map(lambda number : number * number, my_list)
resulting_list = list(result)
print(resulting_list)