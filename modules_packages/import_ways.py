'''import keyword allow us to import all the functionalities
of a module in our script.
To use a module function we have the following syntax:
<module name>.function(<parameters>)'''
import calculator

'''With from ... import ..., every time we want to use a
module functionality we just call the function by its
name: function()'''
from calculator import *

'''If we use asterisk after the import keyword in the from ... import ...
statement we have imported all the module functionalities. If you just
want to import some functionalities then we write the name of the function
or funtions that we want to use separated by comas'''
from calculator import plus, subtraction

# Import on multiple lines
'''In Python you can break a logical line into two or more
physical lines, there are two ways:'''

'''The first way is enclosing the list of imported packages
in parentheses and give as many line breaks as needed:'''
from calculator import (plus, 
			subtraction,
                        multiplication, 
                   divide) 
'''Indentation doesn't matter but it is recommended to be
consistent'''

'''The second way is using backslash before each line break:'''
from calculator import plus, \
			subtraction, \
                        multiplication, \
                   divide
'''Indentation doesn't matter too but it is recommended to be
consistent too'''

# Rename objects
from calculator import plus as my_sum

result = my_sum(4, 6)
print(result)

'''NOTE 1: A physical line is a line as we see it on our
text editor each one below the prior line. A logical line is
an entire statement line which can be extend undefinedly and
that our text editor enumerates it and sometimes wraps it
in multiple physical lines

NOTE 2: Backslashes don't only can be used on import statements
but on any statement such as value assignation, if-statements,
comprehensions, and so on

NOTE 3: Backslashes are not needed if we are using parentheses, 
square brackets or curly brackets'''