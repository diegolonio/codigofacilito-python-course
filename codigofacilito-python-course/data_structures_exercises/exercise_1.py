# Given a dictionary which contains the student's notes, the keys are the subjects'
# names and the values are the subjects' notes. Show on screen the student's average note.
# =======================================================================================

def average_note(students_notes):
    return sum(students_notes.values()) / len(students_notes)

if __name__ == '__main__':
    students_notes = {'Maths': None, 'Literature': None, 'History': None, 'Chemistry': None, 'Biology': None}

    for subject in students_notes:
        students_notes[subject] = int(input('\nPlease enter the note for {} subject: '.format(subject)))

    print('\n==================================')
    print('\nThe student\'s average note is: {}\n'.format(average_note(students_notes)))