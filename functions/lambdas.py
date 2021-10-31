def celsius_to_farhenheit(grades):
    return grades * 1.8 + 32
variable_function = celsius_to_farhenheit
farhenheit_grades = variable_function(32)
print(farhenheit_grades)

'''celsius_to_farhenheit() function converted into a
lambda function'''
my_function = lambda grades=0 : grades * 1.8 + 32
farhenheit_grades = my_function(32)
print(farhenheit_grades)