'''As we mentioned before, once we defined a function, we can call it
n-times, even out of our script, as we will see forward. That is why a
good programming practice is document our functions.
To document a function we will do it with a comment, which will be located
inside of the function and using triple quotes as we can see in the next
example'''
def my_function(*args):
    '''This is the documentation of a function'''
    print(args)

'''We can work with the documentation using the attribute __doc__'''
print(my_function.__doc__)

# =================================================================
'''Now let's see an example where we can benefit from our documentation'''
def plus(a, b):
    """Plus function"""
    return a + b

def subtraction(a, b):
    """Subtraction function"""
    return a - b

options = {'a': plus, 'b': subtraction}
for option, function in options.items():
    message = '{}) {}'.format(option, function.__doc__)
    print(message)
option = input('Enter the desired option (a/b): ')
print('You selected:', options[option].__doc__)

'''We store the functions inside our dictionary,
then we iterate the items in the dictionary and in each
iteration we display the documentation'''