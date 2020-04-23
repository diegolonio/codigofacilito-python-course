# Show on the screen the number of vowels in a phrase given by the user.
# ======================================================================

VOWELS = 'aeoiu'

def phrase_vowels(phrase : str) -> int:
    phrase = phrase.lower()
    counter = 0

    for vowel in VOWELS:
        if vowel in phrase:
            counter += 1

    return counter

if __name__ == '__main__':
    users_phrase = input('Please, enter a phrase: ')
    print('\nThere are {} vowels in the given phrase.'.format(phrase_vowels(users_phrase)))