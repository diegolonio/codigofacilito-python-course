text = 'python 3 course'

"""
capitalize() function converts the text in
sentence format with first letter capitalized
"""
text = text.capitalize()
print(text)

"""
swapcase () function switches between uppercase
and lowercase depending on the text format
"""
text = text.swapcase()
print(text)

# upper() function changes all the text to uppercase
text = text.upper()
print(text)

# lower() function changes all the text to lowercase
text = text.lower()
print(text)

# isupper() function indicates if the text is uppercase
print(text.isupper())

# islower() function indicates if the text is lowercase
print(text.islower())

# title() function gives a title format to text
text = text.title()
print(text)

"""
replace() function replaces all the occurrences 
of the string given in the first parameter in the 
string which the method is applied to with the 
string given in the second parameter
"""
text = text.replace('o', ' replace ')
print(text)

"""
There is a third parameter for replace() function, and it indicates
the n-first occurrences to replace in the string which the method is 
applied of the string given in the first parameterto with the
string given in the second parameter
"""
text = text.replace(' replace ', ' another replace ', 2)
print(text)

"""
strip() function removes whitespaces at the beginning and at the
end of the text
"""
text = "    python 3 course   "
text = text.strip()
print(text)

# Another useful functions for strings
course = 'python'
version = '3'

text = '%s %s course'%(course, version)
print(text)

text = '{} {} course'.format(course, version)
print(text)

text = '{a} {b} course'.format(a=course, b=version)
print(text)

text = '{b} {a} course'.format(a=course, b=version)
print(text)

text = '{a} {b} course'.format(b=version, a=course)
print(text)