"""
File: Lsn19-future_from-present
Author: Jacob Hildebrand
Date: 02/18/2023
Purpose: calculate future investment
"""
#Pupose
print('This program will calculate the future value from annual investments\n')

# Define the annual investment amount, interest rate, and investment period
annual_investment = float(input("How much is the annual investment (in dollars)? "))
interest_rate = float(input("What is the annual interest rate (enter 0.05 for 5%)? "))
investment_period = int(input("How long is the investment (in years)? "))

# Calculate the future value of the investment using the formula:
# future_value = annual_investment * ((1 + interest_rate) ** investment_period - 1) / interest_rate

future_value = annual_investment * ((1 + interest_rate) ** investment_period - 1) / interest_rate

# Print out the result
print("\n${:.2f} deposited each year at {:.2f}% annual interest will be worth ${:.2f} in {} years.".format(
    annual_investment, interest_rate * 100, future_value, investment_period))