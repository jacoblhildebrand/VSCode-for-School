"""
File: Lsn20-meal_price_program
Author: Jacob Hildebrand
Date: 02/23/2023
Purpose: 
"""
#State Pupose
print('This program will calculate the total price of a meal.\n')
#User input
child = float(input("What is the price of a childs meal (in dollars)? "))
adult = float(input("What is the price of an adult meal (in dollars)? "))
num_child = int(input('How many children are there? '))
num_adult = int(input('How many adults are there? '))
sales_tax = float(input('What is the sales tax rate (enter 0.05 for 5%)? '))
#Calculate Tips and tax
subtotal = child*num_child + adult*num_adult
fifteen_tip = subtotal*.15
eighteen_tip = subtotal*.18
twenty_tip = subtotal*.20
sales_tax_amount = subtotal*sales_tax

#Suggested tip amounts
print(f'\nSuggested Tip Amounts:')
print(f'    15% = ${fifteen_tip:.2f}')
print(f'    18% = ${eighteen_tip:.2f}')
print(f'    20% = ${twenty_tip:.2f}')
#User inputs tips
tip_amount = float(input('\nPlease enter a tip amount (in dollars): '))

#Total is Calculated
total = subtotal+sales_tax_amount+tip_amount

#Display Subtotal, Sales tax, Tip, and Total
print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax_amount:.2f}')
print(f'Tip: ${tip_amount:.2f}')
print("---------------------------")
print(f'Total: ${total:.2f}')

payment = float(input('\nWhat is the payment amount (in dollars)? '))
change = payment-total
print(f'Change: ${change:.2f}')

print('\nThank you for Dining with us!')