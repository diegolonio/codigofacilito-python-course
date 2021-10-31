'''With import keyword we import functions from another python
code file to the current file we are working in'''
import calculator

result = calculator.plus(8, 7)
print(result)

# It displays: calculator
print(calculator.__name__)

# The file we execute have as __name__: __main__
print(__name__)