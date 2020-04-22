# Given a dictionary which contains the student's notes, the keys are the subjects'
# names and the values are the subjects' notes. Show on screen the studen's average note.
# =======================================================================================

def average_note(dictionary):
    return sum(dictionary.values()) / len(dictionary)

if __name__ == '__main__':
    my_dict = {'Maths': None, 'Literature': None, 'History': None, 'Chemistry': None, 'Biology': None}

    for key, value in my_dict.items():
        my_dict[key] = int(input('\nPlease enter the note for {} subject: '.format(key)))

    print('\n{}\n'.format(average_note(my_dict)))