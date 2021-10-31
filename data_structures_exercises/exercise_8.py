# Show on the screen how often vowels appear in a given phrase by the user.
# =========================================================================

VOWELS = 'aeiou'

def vowels_frecuencies_in_phrase(phrase : str) -> tuple:
    phrase = phrase.lower()

    for vowel in VOWELS:
        if vowel in phrase:
            yield (vowel, phrase.count(vowel))

if __name__ == '__main__':
    users_phrase = input('Please, enter a phrase: ')
    print('\nThe frequency of each vowel that appears in the given phrase is:')

    for vowel, frequency in vowels_frecuencies_in_phrase(users_phrase):
        print('\n- {} -> {} times'.format(vowel.upper(), frequency))