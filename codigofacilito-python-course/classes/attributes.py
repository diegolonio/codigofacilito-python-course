class User:
    def __init__(self, name='', username='', email=''):
        self.name = name
        self.username = username
        self.email = email
    def greeting(self):
        return 'Hello {} I am an user'.format(self.name)
    def show_user(self):
        print(self.username)
    def show_name(self):
        print(self.nombre)
diego = User('Diego Apolonio', 'diego.apoloniov@gmail.com', 'diegolonio')

print(diego.name)