'''Class methods are similar to static methods because they
can be used without need to instance the class'''

E = 2.718281828

# Instance method
class Circle:
    pi = 3.14159265
    def area(self):
        return self.pi * self.ratio**2
circle = Circle()
circle.ratio = E**2
area = circle.area()
print(area)

# Class method
class Circle:
    pi = 3.14159265
    @classmethod
    def area(cls, ratio):
        return cls.pi * ratio**2
'''Class methods must to receive parameters, you can
use any other word, but by convention we use cls'''

area = Circle.area(E)
print(area)