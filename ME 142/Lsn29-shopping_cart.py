"""
Jacob Hildebrand
Lsn28-shjopping_cart
3/16/23
Make and maintain a shopping list
"""

# initialize empty lists for items and prices
items = []
prices = []

# display the menu and get user input
def display_menu():
    print("Welcome to the Shopping Cart Program!\n")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. List items & total price")
    print("3. Remove item")
    print("4. Quit")

    return int(input("Which option do you want? "))

# add an item and its price to the lists
def add_item():
    item = input("\nWhat item would you like to add? ")
    price = float(input("What is the price of " + item + "? $"))
    items.append(item)
    prices.append(price)
    print(item + " has been added to your cart.\n")

# display all items in the cart and their total price
def list_items():
    print("\nThe contents of the shopping cart are:")

    total = 0
    for i in range(len(items)):
        print(str(i+1) + ".   " + items[i] + "      $" + str(prices[i]))
        total += prices[i]

    print("\nThe total price of these items is $" + str(total) + "\n")

# remove an item from the cart
def remove_item():
    index = int(input("\nWhich item number would you like to remove? ")) - 1

    if index >= len(items) or index < 0:
        print("\nYou don't have " + str(index+1) + " items in your cart.")
        print("Please select another option.\n")
    else:
        item = items.pop(index)
        price = prices.pop(index)
        print("\n" + item + " has been removed from your cart.\n")

# run the program
choice = display_menu()

while choice != 4:
    if choice == 1:
        add_item()
    elif choice == 2:
        list_items()
    elif choice == 3:
        remove_item()
    else:
        print("\nThat is an invalid entry. Please select again.\n")

    choice = display_menu()

print("\nThank you for shopping with us. Goodbye.")