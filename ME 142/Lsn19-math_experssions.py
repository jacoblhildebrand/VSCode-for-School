"""
File: Lsn19-math_expressoins
Author: Jacob Hildebrand
Date: 02/18/2023
Purpose: Evaluate Math Expressions and calculate are of circle
"""
import math

#Evaluate and diplay result of Math expressoin
y = 3/(2-math.sqrt(7))-6*4+2**2
print(f'\nThe value of the expression is {y:.3f}')
print()

#Prompt for radius
radius = input('What is the radius of the cirlce? ')

#Calculate area of cirle and display
area = math.pi*float(radius)**2
print(f'The area of the circle is {area:.3f}')
