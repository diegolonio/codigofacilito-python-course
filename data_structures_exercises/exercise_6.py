# Replace each letter of a phrase given by the user with its position in the alphabet
# and show the new string on the screen. (Whitespaces are not replaced)
# ===================================================================================

ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'

def letters_positions(phrase : str) -> str:
    phrase = phrase.lower()

    for letter in phrase:
        if letter == ' ':
            continue
        phrase = phrase.replace(letter, str(position_in_alphabet(letter)))

    return phrase

def position_in_alphabet(character : str) -> int:
    return ALPHABET.index(character) + 1

if __name__ == '__main__':
    users_phrase = input('Please, enter a phrase: ')
    print(letters_positions(users_phrase))