'''A package is a folder that contains multiple python code files,
it is, modules'''

# Importing functions from different modules
from animals.birds import Penguin
from animals.felines import Lion

# Importing all modules
from animals import *

# Importing directly using the statement in the __init__.py file
from animals import Penguin

# Importing an instance of a class
from animals import my_jaguar

# Importing a function
from animals import my_function

my_function()

my_jaguar.hunt()

penguin = Penguin()
lion = Lion()

penguin.swim()
lion.roar()