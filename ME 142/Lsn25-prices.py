#create and display list of items and prices

#input
num_items = int(input('\nHow many items do you need to enter prices for? '))

#lists
items = []
prices = []

#build lists
for i in range(num_items):
    new_item = input(f'\nWhat is item #{i+1}? ').capitalize()
    new_price = float(input(f'What is the price of {new_item}? $'))
    items.append(new_item)
    prices.append(new_price)

#print results
print('\nItem       Price')
for i in range(len(items)):
    print(f'{items[i]:<10} ${prices[i]:.2f}')

#summary Stats
max_price = prices[0]
max_item = items[0]
for i in range(len(items)):
    if prices[i]>max_price:
        max_price = prices[i]
        max_item = items[i]

print()
print(f'The total price of all the items is ${sum(prices):.2f}.')
print(f'{max_item} had the highest price of ${max_price}.\n')
