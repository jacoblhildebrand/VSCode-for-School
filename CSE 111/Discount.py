from datetime import datetime

def calculate_discount(subtotal):
    discount = 0.0
    if subtotal >= 50:
        discount = subtotal * 0.10
    return discount

def main():
    current_date_and_time = datetime.now()
    day_of_week = current_date_and_time.weekday()  # 0=Monday, 1=Tuesday, 2=Wednesday, ..., 6=Sunday

    subtotal = 0.0
    while True:
        price_input = input("Please enter the price (or 0 to finish): ")
        price = float(price_input)
        if price == 0:
            break
        quantity = int(input("Please enter the quantity: "))
        subtotal += price * quantity

    discount_amount = calculate_discount(subtotal)
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax - discount_amount

    # Print results
    if day_of_week == 1 or day_of_week == 2:  # Tuesday or Wednesday
        if discount_amount > 0:
            print(f"Discount amount: {discount_amount:.2f}")
        else:
            amount_needed = 50 - subtotal
            print(f"You need to spend an additional ${amount_needed:.2f} to qualify for the discount.")
    
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")

if __name__ == "__main__":
    main()