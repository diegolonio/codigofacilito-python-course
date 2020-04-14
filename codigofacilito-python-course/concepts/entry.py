"""
(1st Method) As we write the answer, it will be
displayed below the question
"""
print('What is your name?:')
name = input()

"""
(2nd Method) As we write the answer, it will be
displayed next to the colons
"""
name = input('What is your name?: ')
# ============================================================
# By the 1st method
print('What is your age?:')
age  = int(input())

# By the 2nd method
age = int(input('What is your age?: '))
# ============================================================
# By the 1st method
print('What is your weight?:')
weight = float(input())

# By the 2nd method
weight = float(input('What is your weight?: '))
# ============================================================
# By the 1st method
print('Are you authorized? (yes/no):')
authorization = input() == 'yes' 

# By the 2nd method
authorization = input('Are you authorized? (yes/no): ') == 'yes'
# ============================================================
print('Hello', name)
print('Age:', age)
print('Weight:', weight)
print('Authorization:', authorization)

"""
NOTE 1: input() function always returns a string

NOTE 2: int() and float() functions converts a number or a string
into an integer or floating-point number, respectively

NOTE 3: In line 30 and 33 compares if the entry is equal to
the string 'yes' and assigns True or False to the variable
"""