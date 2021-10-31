'''Static methods can be used without instantiaing the class.'''

# Instance method
class Triangle:
    def area(self):
        return (self.base * self.height) / 2
triangle = Triangle()

triangle.base = 10
triangle.height = 20
result = triangle.area()
print(result)

# Static method
class Triangle:
    @staticmethod
    def area(base, height):
        return (base * height) / 2

result = Triangle.area(10, 21)
print(result)