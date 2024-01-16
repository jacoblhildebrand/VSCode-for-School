"""
File: Lsn20-temp_conversion
Author: Jacob Hildebrand
Date: 02/23/2023
Purpose: Cionvert from fahrenheit to celcius
"""

# Lsn20-temp_conversion.py

# Get the temperature in Fahrenheit from the user
fahrenheit = float(input("What is the temperature in Fahrenheit? "))

# Convert the temperature to Celsius using the formula
celsius = (fahrenheit - 32) * 5 / 9

# Print out the result
print("\n{:.1f} degrees Fahrenheit = {:.1f} degrees Celsius".format(fahrenheit, celsius))