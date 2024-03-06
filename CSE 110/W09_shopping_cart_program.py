#empty list to store the items in the shopping cart
shopping_cart = []

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
    shopping_cart.append(item)
    print(f"'{item}' has been added to the cart.")

#display the items in the cart
def view_cart():
    print("\nThe contents of the shopping cart are:")
    for index, item in enumerate(shopping_cart, start=1):
        print(f"{index}. {item}")

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
            print("N/A.")
        elif choice == '4':
            print("N/A.")
        elif choice == '5':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#execute main function
if __name__ == "__main__":
    main()