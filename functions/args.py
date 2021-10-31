# Functions with n-parameters
def plus(*args):
    total = 0
    for value in args:
        total += value
    return value
result = plus(3, 67, 13, 56)
print(result)

'''Double asterisk returns a dictionary where key is
the name of the parameter'''
def authenticated(**kwargs):
    print(kwargs)
authenticated(auto=True, img=False)

def combination(required, *args, **kwargs):
    print(required)
    print(args)
    print(kwargs)
combination('Required value', 10, 20, 30, v1=True, v2=False)