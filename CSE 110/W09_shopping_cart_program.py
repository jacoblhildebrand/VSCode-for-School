#empty list to store the items in the shopping cart
shopping_cart_items = []
shopping_cart_prices = []

#display the menu
def display_menu():
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

#add item to the cart
def add_item():
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? $"))
    shopping_cart_items.append(item)
    shopping_cart_prices.append(price)
    print(f"'{item}' has been added to the cart.")

#display the items in the cart
def view_cart():
    print("\nThe contents of the shopping cart are:")
    for index, (item, price) in enumerate(zip(shopping_cart_items, shopping_cart_prices), start=1):
        print(f"{index}. {item} - ${price:.2f}")

# Function to remove item from the cart
def remove_item():
    view_cart()
    if shopping_cart_items:  # Check if cart is not empty
        try:
            index = int(input("Which item would you like to remove? ")) - 1
            if 0 <= index < len(shopping_cart_items):
                removed_item = shopping_cart_items.pop(index)
                removed_price = shopping_cart_prices.pop(index)
                print(f"'{removed_item}' removed from the cart.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("The shopping cart is empty.")

# Function to compute total price of items in the cart
def compute_total():
    total_price = sum(shopping_cart_prices)
    print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

# Main function
def main():
    print("Welcome to the Shopping Cart Program!")
    while True:
        display_menu()
        choice = input("Please enter an action: ")
        if choice == '1':
            add_item()
        elif choice == '2':
            view_cart()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            compute_total()
        elif choice == '5':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#execute main function
if __name__ == "__main__":
    main()