#num = 0
#count=0
#sum=0
#print()
#while num<10:
#   num=int(input('Please enter and integer: '))
#   if num<10:
#        count+=1
#        sum+=num
#
#print(f'\nYou entered {count} integers that were less than 10')
#print(f'The sum of those {count} integers was {sum}\n')


friends = []
add_friends='initialize'
print()

while add_friends!='End':
    add_friends=input("Enter a friend's name (or 'end' to quit): ").capitalize()
    if add_friends!='End':
        friends.append(add_friends)

print(f'\nYou have {len(friends)}')
print(f'Your friends are {friends}\n')

