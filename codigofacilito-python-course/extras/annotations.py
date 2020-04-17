'''Annotations allow us to indicate the data type of each
parameter of our function as well as the data type of the
returned value.

It is important to remark that annotations are just
suggestions of the expected data type of parameters,
but actually it is not a rule, it means that you can
still passing any value despite of its data type to the
function even when the function have an annotation that
says it just receives integer parameters'''

# Function without annotations
def greeting(name, number):
    print('Hello ' + name, '\nAge: ' + str(number))

# Function with annotations
def greeting(name : str, number : int) -> None:
    print('Hello ' + name, '\nAge: ' + str(number))

# Function with annotations and values by default
def greeting(name : str = 'Anónimo', number : int = 18) -> None:
    print('Hello ' + name, '\nAge: ' + str(number))

greeting()