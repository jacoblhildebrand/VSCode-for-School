#Demo nested if statement
choice1 =input('Do you want ot go IN or OUT?')
if choice1.lower() == 'in':
    choice2a = input('Do you want to go LEFT or RIGHT?')
    if choice2a.lower() == 'left':
        print('This is result1')
    elif choice2a.lower() == 'right':
        print('This is result2')
    else:
        print('You did not enter a valid option.')
elif choice1.lower() == 'out':
    choice2b = input('Do you want to go UP or DOWN?')
    if choice2b.lower() == 'up':
        print('This is reulst3')
    elif choice2b.lower() == 'down':
        print('This is result4')
    else:
        print('You did not enter a valid option.')
else:
    print('You did not enter a valid option.')
