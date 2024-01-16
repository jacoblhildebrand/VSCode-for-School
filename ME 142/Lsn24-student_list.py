students = ['Chris', 'Jack', 'Susan']
grades = [87, 71, 93]

print(f'The current students are {students}.')
print(f'Their grades are {grades}.\n')

action = input('Do you want to ADD or REMOVE a student? ').lower()

if action == 'add':
    name = input('What is the name of the student you want to add? ')
    grade = int(input('What is the grade for the added student? '))
    students.append(name)
    grades.append(grade)
    print(f'\nThe list of your students is now {students}.')
    print(f'Their grades are {grades}.')
elif action == 'remove':
    num = int(input('What is the number of the student to remove? '))
    if num <= len(students):
        students.pop(num-1)
        grades.pop(num-1)
        print(f'\nThe list of your students is now {students}.')
        print(f'Their grades are {grades}.')
    else:
        print('\nInvalid student number.')
else:
    print('\nYou did not enter a valid option.')