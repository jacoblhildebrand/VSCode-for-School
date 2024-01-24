childs_price = float(input("What is the price of a child's meal? "))
adults_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the  sales tax rate? "))
tip_rate = float(input("What percentage tip would you like to leave? "))


subtotal = childs_price*num_children+adults_price*num_adults
print(f"\nSubtotal: ${subtotal:.2f}")
sales_tax = subtotal*(sales_tax_rate/100)
print(f"Sales Tax: ${sales_tax:.2f}")

total_before_tip = sales_tax+subtotal
tip_amount = total_before_tip * (tip_rate / 100)
print (f"Total (before tip): ${total_before_tip:.2f}")

print(f"Tip: ${tip_amount:.2f}")
total = total_before_tip + tip_amount
print(f"Total (with tip): ${total:.2f}")

payment = float(input("\nWhat is the payment amount? "))
change = payment-total
print (f"Change: ${change:.2f}")
