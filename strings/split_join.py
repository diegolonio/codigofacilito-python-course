languages = 'python; java; ruby; php; swift; javascript; c#; c; c++'

"""
split() function splits a string into a list where each 
item is a word of the string
"""
my_list = languages.split()
print(my_list)

"""
By default, the separator is blank space, but you can 
specify a separator by passing it as parameter of the function
"""
my_list = languages.split('; ')
print(my_list)

"""
join() function joins all the list items in an
unique string with the set of characters specified 
in the string which the method is applied to
"""
new_list = ' '.join(my_list)
print(new_list)

text = """This
is a text
with line 
breaks"""

"""
splitlines() function splits a string into a list
where each item is each line in the text.
The separator is \n
"""
text = text.splitlines()
print(text)
