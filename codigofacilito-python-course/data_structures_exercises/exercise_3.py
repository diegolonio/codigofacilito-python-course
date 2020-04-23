# Create a list which store 10 positive numbers entered by the
# user. Show on the screen: the sum of all of the numbers, its
# average, the highest and the smallest number.
# ============================================================

def average(users_numbers):
    return sum(users_numbers) / len(users_numbers)

if __name__ == '__main__':
    users_numbers = list()
    number = 0

    for i in range(1, 11):
        number = int(input('\nPlease, enter the value of #{} number: '.format(i)))
        users_numbers.append(number)

    print('\n========================================')
    print('\nNumbers sum: {}'.format(sum(users_numbers)))
    print('\nNumbers average: {}'.format(average(users_numbers)))
    print('\nHighest number: {}'.format(max(users_numbers)))
    print('\nSmallest number: {}'.format(min(users_numbers)))