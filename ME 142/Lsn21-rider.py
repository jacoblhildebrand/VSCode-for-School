"""
Lsn21-rider
Name: JAcob Hildebrand
Date:2/23/2023
Pupose: Determine if a person may ride a ride at an amusment park.
"""
#input
print()
height = float(input('What is you height in inches? '))
age = int(input('What is your age? '))
riders = (input('How many riders (Single/Multiple)? '))

#Determine if person can ride
if height >= 36 and (age >= 18 or riders.lower() == "multiple"):
    can_ride = True
else:
    can_ride = False

#Display results
if can_ride:
    print('You can ride this ride! Have Fun!')
else:
    print("You can not ride this ride. We're sorry.")
print()