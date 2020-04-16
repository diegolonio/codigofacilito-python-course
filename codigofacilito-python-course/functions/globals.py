'''Any variable that we define outside of any function is
called a global variable'''
animal = 'Dog'
def show_animal():
    print(animal)
show_animal()
print(animal)
'''Global variables may be used inside of any function'''
def show_animal():
    animal = 'Whale'
    print(animal)
show_animal()
print(animal)
'''When a global variable is used within a function,
it becomes a local variable for the function and its
value can be reassigned; but when the function execution
finishes, the variable becomes global again and its value
will be the same as before the variable was used inside
the function. This is because once we define the variable
inside the function, Python considers the variable outside
the function is not equal to the variable inside the function.
Because they are in different contexts'''

'''To be able to change the value of a global variable
inside a function we use the keyword: global'''
def show_animal():
    global animal
    animal = 'Whale'
    print(animal)
show_animal()
print(animal)