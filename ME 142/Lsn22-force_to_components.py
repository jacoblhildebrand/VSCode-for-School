"""
Jacob Hildebrand
Lsn22-force_to_components
2/24/2023
"""

#Given a force and an angle, fond the x and y components

import math
print()

#input
force = float(input('What is the magnitude of the force (in lbs)? '))
angle = float(input('What is the angle of the force (in degrees)? '))

#calculate
fx = force * math.cos(math.radians(angle))
fy = force * math.sin(math.radians(angle))

#print
print()
print(f'The x component of the force is {fx:.1f} lbs.')
print(f'The y component of the force is {fy:.1f} lbs.')
print()