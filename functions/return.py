'''If we don't indicate a value to return in a function,
it will return None by default'''
def my_function():
    print('a message')
returned_value = my_function()
print(returned_value)

'''We can indicate to the function what to return with
the keyword: return'''
def my_second_function():
    print('another message')
    return 2
returned_value = my_second_function()
print(returned_value)

'''NOTE: The function execution ends until the
return statement is executed'''