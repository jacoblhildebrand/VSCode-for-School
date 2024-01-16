"""
File: Lsn19-unit_conversion_psi
Author: Jacob Hildebrand
Date: 02/18/2023
Purpose: convert ft/s to mph
"""
lbs_inch = input('Please enter pressure in lbs/ft^2 ')
inches_per_foot = 12

#convert pressure to psi
psi = float(lbs_inch)/inches_per_foot/inches_per_foot

print(f'{psi:.3f} PSI')