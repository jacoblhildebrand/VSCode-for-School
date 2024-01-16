#Create and display lists of items and prices

#Display mesage to the user
print('\nEnter items and thier corresponding prices')

#Initialize lists and variables
items=[]
prices=[]
item = 'initial value'


#Build lists
while item != 'End':
    item = input(f"\nWhat item do you want to add ('End' to quit)? ").capitalize()
    if item != 'End':
        price = float(input(f'What is the price of {item.lower()}? $'))   
        items.append(item)
        prices.append(price)

#Print results
print('\nItem       Price')
for i in range(len(items)):
    print(f'{items[i]:<10} ${prices[i]:.2f}')

#calculate
max_price = prices[0]
max_item = items[0]

for i in range(len(items)):
    if prices[i]>max_price:
        max_price=prices[i]
        max_item=items[i]

print(f'The total price of all the items is ${sum(prices):.2f}')
print(f'{max_item} had the highest price of ${max_price}\n')