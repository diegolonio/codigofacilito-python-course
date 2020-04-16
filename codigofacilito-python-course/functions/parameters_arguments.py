# Functions with parameters
def create_user(name, surname, age):
    return {
        'name': name,
        'surname': surname,
        'complete_name': '{} {}'.format(name, surname),
        'age': age
    }
name = input('What is your name?: ')
surname = input('What is your surname?: ')
age = int(input('What is your age?: '))
user = create_user(name, surname, age)
print(user['name'])
print(user['surname'])
print(user['age'])

# Default parameters
def greeting(name='Anonymus'):
    return 'Hello {} welcome to the Python 3 Course'.format(name)
message = greeting('Karen')
print(message)