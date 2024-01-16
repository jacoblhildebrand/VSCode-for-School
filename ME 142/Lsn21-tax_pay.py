

# Get the amount paid from the user
amount_paid = float(input("How much did you pay? "))

# Check if the amount paid is greater than 1.00
if amount_paid > 1.00:
    tax_rate = 0.07
else:
    tax_rate = 0

# Print out the tax rate
print("The tax rate is: {:.2f}".format(tax_rate))