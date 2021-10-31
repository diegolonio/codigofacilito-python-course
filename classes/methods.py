class User:
    pass
    def greeting(self, name):
        return 'Hello {} I am an user'.format(name)
'''All the class methods must to receive parameters, by
default they receives 'self', you can use any other word
but by convention we use 'self' '''

diego = User()
massage = diego.greeting('Diego')
print(massage)