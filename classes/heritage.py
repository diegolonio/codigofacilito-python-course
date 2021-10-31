class Animal:
    def eat(self):
        print('Eating')
    def sleep(self):
        print('Sleeping')
    def common(self):
        print('Animal method')

class Pet():
    def adoption_date(self, date):
        self.adoption_date = date
    def common(self):
        print('Pet method')

class Dog(Animal, Pet):
    def __init__(self, name):
        self.name = name
    def bark(self):
        print('Barking')
    def common(self):
        print('Dog method')

rocko = Dog('Rocko')

rocko.sleep()
rocko.eat()
rocko.bark()
rocko.adoption_date('Today')
'''If child class and parent class have a common method, the executed
method will be the method from the instantiated class.
If the instantiated class doesn't have the common method, it will
search in the parent classes from left to right of the heritage
parameters of the instantiated class'''
rocko.common()
date = rocko.adoption_date 
print(date)

class Cat(Animal):
    def purr(self):
        print('Purr uwu')
fuzz = Cat()

fuzz.purr()
fuzz.sleep()