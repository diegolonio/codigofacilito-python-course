title = 'Python 3 Course'
'''In this case, once the logical condition is met
the for loop is broken and the iterations ends''' 
for character in title:
    if character is ' ':
        break
    print(character)

'''In this case, once the logical condition is met
the current iteration is skipped and iterations continues'''
for character in title:
    if character is ' ':
        continue
    print(character)