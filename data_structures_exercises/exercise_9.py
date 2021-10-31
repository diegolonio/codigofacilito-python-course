# Remove the vowels in a given phrase by the user and show on the screen the new
# string.
# ==============================================================================

VOWELS = 'aeiou'

def remove_vowels(phrase :str ) -> str:
    phrase = phrase.lower()

    for vowel in VOWELS:
        if vowel in phrase:
            phrase = phrase.replace(vowel, '')
    
    return phrase.strip()

if __name__ == '__main__':
    users_phrase = input('Please, enter a phrase: ')
    print('\nThe new string is: {}'.format(remove_vowels(users_phrase)))