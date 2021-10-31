# There's two ways to declare a class:
class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        # In this case we return the name attribute
        return self.name
'''When we create an instance of a class and we display it,
the next message is shown:

<__main__.(class name) object at (memory address)>

to be able to change what is shown when we display the class
we have to do:'''

class Duck(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

'''It might seem that the Cat class is inheriting nothing from any
other class and Duck class does. Though, both classes are inheriting
attributes and methods from the Object class, it is just that in the
declaration of Duck class we are doing it explicitly'''

my_cat = Cat('Whiskers')
my_duck = Duck('Daffy')

print(my_cat)
print(my_duck)

# Know the our object instance attributes
print(my_cat.__dict__)
print(my_duck.__dict__)