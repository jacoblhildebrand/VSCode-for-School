"""
File: Lsn19-future_from-present
Author: Jacob Hildebrand
Date: 02/18/2023
Purpose: calculate future investment
"""
investment = input('How much is the one-time present investment (in dollars)? ')
interest = input('What is the annual interest rate (enter 0.05 for 5%)? ')
years = input('How long is the investment (in years)? ')

#Calculate and display
final_value = float(investment)*(1+float(interest))**float(years)

print(f'${float(investment):.2f} deposited now at {float(interest):.2f}% annual interest will be worth ${final_value:.2f} in {int(years)} years.')
