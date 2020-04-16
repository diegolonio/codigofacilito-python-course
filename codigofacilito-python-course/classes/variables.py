'''Instance variables values changes on each instance.
If you change an instance variable value, instance variable value of
other instances won't change because instance variables are unique
for each instance'''

'''Class variables values do not change in any instance.
As the same way than instance variables, if you change a class
variable value of an instance, it won't change in any other instance'''

class Circle:
    pi = 3.14159265 # Class variable
    def __init__(self, ratio):
        self.ratio = ratio # Instance variable

# Instance variables
circle_a = Circle(10)
circle_b = Circle(20)
circle_b.ratio = 100
print(circle_a.ratio)
print(circle_b.ratio)

# Class variables
print(circle_a.pi)
print(circle_b.pi)

# We can call to class variables without instantiating
print(Circle.pi)

'''If a class variable value changes without instantiating,
its value changes in all the instances'''
Circle.pi = 4
print(circle_a.pi)
print(circle_b.pi)