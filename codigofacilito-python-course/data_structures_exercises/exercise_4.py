# Given a list of phrases entered by the user, show on the screen
# all those that are palindromes.
# ===============================================================

def is_palindrome(phrase):
    phrase = phrase.lower().replace(' ', '')
    return phrase == phrase[::-1]

if __name__ == '__main__':
    users_phrases = list()
    number_of_phrases = int(input('\nEnter the number of phrases you want to enter: '))
    current_phrase = ''

    for i in range(number_of_phrases):
        current_phrase = input('\nEnter phrase #{}: '.format(i + 1))
        users_phrases.append(current_phrase.capitalize())

    print('\n=================================')
    print('\nThe phrases: ')

    for phrase in users_phrases:
        if is_palindrome(phrase):
            print('\n- {}'.format(phrase))

    print('\nAre palindromes.')