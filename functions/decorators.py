'''
To be able to work with decorators we have to consider
that we will have to work with at least three functions
function_a(function_b):
    return function_c
'''
def decorator(function):
    def new_function():
        print('We can add code before')
        function()
        print('We can add code after')
    return new_function

'''pass indicates to the Python interpreter that for the
moment the function will do nothing'''
@decorator
def decorated_function():
    print('This is a decorated function')

decorated_function()
print('\n')

'''To decorate functions with parameters we use
asterisks and double asterisks'''
def decorator(function):
    def new_function(*args, **kwargs):
        print('We can add code before')
        result = function(*args, **kwargs)
        print('We can add code after')
        return result
    return new_function

@decorator
def plus(val1, val2):
    return val1 + val2
result = plus(23, 65)
print(result)