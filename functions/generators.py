'''Generators in Python are a special type of functions
that we can use to create a sequence of data'''

def multiplication_table(number, maximum=10):
    for position in range(1, maximum + 1):
        yield number, position, number * position
# yield returns one value on each iteration of the loop

for number, position, result in multiplication_table(2):
    print(number, '*', position, '=', result)

'''rango() function will return one value of the interval
specified on each iteration'''
def rango(start, end):
    counter = start - 1
    while counter < end - 1:
        counter += 1
        yield counter