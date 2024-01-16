"""
File: Lsn19-unit_conversion_mph
Author: Jacob Hildebrand
Date: 02/18/2023
Purpose: convert ft/s to mph
"""
feet_sec = input('Please enter speed in feet per second ')
feet_in_miles = 5280
sec_per_minute = 60
min_per_hour = 60

#convert speed to mph
miles_per_hour = float(feet_sec)/feet_in_miles*sec_per_minute*min_per_hour

print(f'{miles_per_hour:.2f} MPH')

