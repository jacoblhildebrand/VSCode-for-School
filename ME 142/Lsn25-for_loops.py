# friends = ['Bob','Julie','Sam']
# for friend in friends:
#     print(friend)

# numbers = [0,1,2,3]
# for number in numbers:
#     print (number)

# name = 'Jim'
# for letter in name:
#     print(letter,end='')

#x = [0,1,2]
# names = ['Jim','Bob','Sally']
# for value in range(len(names)):
#     print(names[value])

#Demo using a for loop to do a calculation on a lost of numbers
# x = [0,1,2,3,4,5]
# y = [0,0,0,0,0,0]
# for i in range(len(x)):
#     y[i] = 4 * x[i]**2 - 2 * x[i] + 5

# print()
# print(f'The x values are {x}')
# print(f'The y values are {y}')
# print()

#Use a for loop to calculate summary statistics on a list of numbers
scores = [67,72,48,77,92]
sum = 0
max = scores[0]
min = scores[0]
for i in range(len(scores)):
    sum = sum + scores[i]
    if scores[i]> max:
        max=scores[i]
    if scores[i]<min:
        min=scores[i]
print()
print(f'The scores are {scores}')
print(f'The sum of the scores is {sum}')
print(f'The average of the scores is {sum/len(scores)}')
print(f'The maximun of the scores is {max}')
print(f'The minumum of the scores is {min}')
adj_ave = (sum-min)/(len(scores)-1)
print(f'The adj. average of the scores is {adj_ave}')
print()
