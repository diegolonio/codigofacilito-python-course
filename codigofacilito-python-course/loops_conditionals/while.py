number = 1234567890
counter = 0
while number >= 1:
    counter += 1
    number /= 10
else:
    print('Loop ends')
print('The number of digits in the number is', counter)