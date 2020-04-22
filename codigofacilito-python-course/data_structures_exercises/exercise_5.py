# Show on screen the most repeated word next to the number
# of repetitions in the chapter 1 of Frankenstein.
# ========================================================

from frankenstein import chapter_one

def most_repeated_words(text : str) -> dict:
    words_repetitions = words_with_repetitions(text)
    max_number_of_repetitions = max(words_repetitions.values())
    most_repeated_words = dict()

    for word in words_repetitions.items():
        if word[1] == max_number_of_repetitions:
            most_repeated_words.update([word])

    return most_repeated_words

def words_with_repetitions(text : str) -> dict:
    text_splitted = text.lower().split(' ')
    words_listed = list_of_words(text)
    words_repetitions = dict()

    for word in words_listed:
        words_repetitions.update({word: text_splitted.count(word)})

    return words_repetitions

def list_of_words(text : str) -> list:
    return list(set(text.lower().split(' ')))


if __name__ == '__main__':
    words = most_repeated_words(chapter_one)
    print('The most repeated word(s) in chapter one\nof the Spanish edition of Frankenstein\'s book is/are: ')
    
    for word, repetitions in words.items():
        print('\n- \'{}\' with {} repetitions'.format(word, repetitions))