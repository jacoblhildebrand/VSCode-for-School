"""
File: Lsn19-volume_cylinder
Author: Jacob Hildebrand
Date: 02/18/2023
Purpose: Calculate volume of cylinder
"""
import math
radius = input('What is the radius of the cylinder? ')
length = input('What is the length of the cylinder? ')
print()
#Calculate and Display
Volume = math.pi*float(radius)**2*float(length)

print(f'The Volume fo the cylinder is {Volume:.3f} units cubed')