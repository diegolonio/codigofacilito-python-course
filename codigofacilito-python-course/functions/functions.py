def greeting():
    print('Hello World')
greeting()

def create_message(name):
    message = 'Hello {} welcome to the Python 3 Course'.format(name)
    return message
name = input('What is your name?: ')
message = create_message(name)
print(message)

def plus(val1, val2, val3):
    return val1 + val2 + val3
result = plus(32, 45, 78)
print(result)

def get_course():
    return 'Basic', 'Python Course', 3.6
level, course, calif = get_course()
print(level, course, calif)