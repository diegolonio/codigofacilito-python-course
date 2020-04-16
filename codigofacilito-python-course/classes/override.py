class Animal:
    def eat(self):
        print('Eating')
    def sleep(self):
        print('Sleeping')

class Pet():
    def adoption_date(self, date):
        self.adoption_date = date

class Dog(Animal, Pet):
    def __init__(self, name):
        self.name = name
    def bark(self):
        print('Barking')
# Overriding the sleep method
    def eat(self):
        print(self.name, 'it is sleeping.')
# We add functionalities to the original sleep method
    def sleep(self):
        print(self.name, 'it is sleeping.')
        Animal.sleep(self)
        print('Do not disturb.')

rocko = Dog('Rocko')
rocko.sleep()