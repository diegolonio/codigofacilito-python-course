'''When we work with modules, it's a good programming practice to
document the code, even more, when we are going to make our own
libraries'''

'''Module documentation
This annotation, which should be located at the beginning of the
file, aims to describe the module'''

__author__ = 'Diego Armando Apolonio Villegas'
__copyright__ = 'Copyright 2020, Diegolonio'
__credits__ = ['Codigofacilito', 'Diosito', 'My mom uwu']
__license__ = 'GPL'
__version__ = '1.0.1'
__maintainer__ = 'Diego Armando Apolonio Villegas'
__email__ = 'diego.apoloniov@gmail.com'
__status__ = 'Production'

def function_a():
    """As we know, we can document functions in this way"""
    pass

def function_b():
    """We can
    make line
    breaks
    """
    pass

def function_c(a=0, b=0):
    """We can provide more details of the parameters
    a -- parameter (default 0)
    b -- parameter (default 0)
    """
    pass

class MyModule:
    """Documentation of our function"""
    def metodo(self):
        """Documentation of our method"""
        pass

'''As we can see, our scripts have three functions, a class and its
corresponding documentation.
The first comment is very important because it is there where we
describe the module, what it does, what it doesn't do, how it works,
how to use it, among other annotations that we may need to put.
Later we can put some metadata. The most common metadata are the eight
that we can see almost at the beginning of this file, however if we 
need to add more metadata we can add ours.
NOTE: In order to consider a metadata we must put double underscores
at the beginning and end of the metadata name.
Once we have commented on the script we can document classes and 
functions.
If we require to visualize a module documentation just use the
help() function.'''

import math
help(math)

'''NOTE: To get outside the documentation press q on the keyboard.
In this way we will be documenting our modules without requiring
use additional software'''