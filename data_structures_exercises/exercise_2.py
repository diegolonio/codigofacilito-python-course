# From previous exercise, show the subject(s) with the highest note
# =================================================================

def subjects_with_highest_notes(students_notes):
    highest_note = max(students_notes.values())
    return {subject: note for subject, note in students_notes.items() if note == highest_note}

if __name__ == '__main__':
    students_notes = {'Maths': None, 'Literature': None, 'History': None, 'Chemistry': None, 'Biology': None}

    for subject in students_notes:
        students_notes[subject] = int(input('\nPlease enter the note for {} subject: '.format(subject)))

    students_highest_notes = subjects_with_highest_notes(students_notes)

    print('\n=============================================')
    print('\nThe subject(s) with the highest note(s) is/are: ')
    for subject, note in students_highest_notes.items():
        print('\n{}: {}'.format(subject, note))