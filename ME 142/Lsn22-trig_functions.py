"""
Lsn22-trig_functions
Jacob Hildebrand
2/24/2023
Solve basic trig functions
"""
#solve for unknown values of a right triangle
import math
print()

#scenario 1
A = 75 #degrees
a = 2   #inches
b = a/math.tan(math.radians(A))
print(f'For Scenario 1, the length b is {b:.3f} inches.')

#Scenario 2
a = 3 #inches
c = 5 #inches
B = math.degrees(math.acos(a/c))
print(f'For Scenario 2, the angle B is {B:.3f} degrees.')

#SCenario 3
a = 1   #inches
c = 4   #inches
A = math.degrees(math.asin(a/c))
print(f'For Scenario 3, the angle A is {A:.3f} degrees.')

#Scenrio 4
a = 2   #inches
b = 4   #inches
B = math.degrees(math.atan(b/a))
c = math.sqrt(a**2 + b**2)
print(f'For Scenario 4, the angle B is {B:.3f} degrees.')
print(f'For scenario 4, the length c is {c:.3f} inches.')
