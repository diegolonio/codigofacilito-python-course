message = 'This is a little greater text in what characters length is concerned'

frequency = message.count('text')
print(frequency)

is_in = 'z' not in message
print(is_in)

"""
find() function returns the index of the first letter
in the word specified in the parameter
"""
index = message.find('greater')
print(index)

print(message[index:index+len('greater')])

"""
startswith() function determines if a text starts with
a string specified in the parameter
"""
starts_with = message.startswith('This')
print(starts_with)

"""
endswith() function determines if a text end with
the string specified in the parameter
"""
ends_with = message.endswith('concerned')
print(ends_with)