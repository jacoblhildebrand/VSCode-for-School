"""
Lsn22-trig_functions
Jacob Hildebrand
2/24/2023
Solve basic trig functions
"""

#solve for unknown values of a right triangle
import math
print()

#Scenario 1
A = 25  #degrees
a = 3   #inches
b = a/math.tan(math.radians(A))
c = math.sqrt(a**2 +b**2)
B = math.degrees(math.asin(b/c))
print(f'For Scenario 1, the length b is {b:.3f} inches.')
print(f'For scneario 1, the length c is {c:.3f} inches.')
print(f'For scenario 1, the angle B is {B:.3f} degrees.\n')

#Scenario 2
a = 2 #inches
c = 4 #inches
B = math.degrees(math.acos(a/c))
b = math.sqrt(c**2 - a**2)
A = math.degrees(math.sin(a/c))
print(f'For Scenario 2, the angle B is {B:.3f} degrees.')
print(f'For scenario 2, the length b is {b:.3f} inches.')
print(f'For scenario 2, the angle A is {A:.3f} degrees.\n')

#Scenario 3
b = 1   #inches
c = 3   #inches
a = math.sqrt(c**2 - b**2)
B = math.degrees(math.sin(b/c))
A = math.degrees(math.asin(a/c))
print(f'For Scenario 3, the angle A is {A:.3f} degrees.')
print(f'For scenario 3, the angle B is {B:.3f} degrees.')
print(f'For Scenario 3, the length a is {a:.3f} degrees.\n')
