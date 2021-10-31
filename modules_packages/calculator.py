def plus(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    if b is 0:
        print('Division by zero')
        return None
    return a / b

if __name__ == '__main__':
    print('I am the main script')
else:
    print('I am being used as a module')