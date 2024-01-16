"""
Jacob Hildebrand
Lsn22-force_from_components
2/24/2023
"""
#given x and y components of a force
# find the resultant force and angle
import math

#input
print()
fx = float(input('What is the x-component of the force (in lbs)? '))
fy = float(input('What is the y-component of the force (in lbs)? '))
force = math.sqrt(fx**2 + fy**2)

if fx > 0 and fy > 0:
    angle = math.degrees(math.atan(fy/fx))
elif fx<0 and fy>0:
    angle = math.degrees(math.atan(fy/fx)) + 180
elif fx<0 and fy<0:
    angle = math.degrees(math.atan(fy/fx)) + 180
elif fx>0 and fy<0:
    angle = math.degrees(math.atan(fy/fx)) + 360
elif fx==0 and fy>0:
    angle = 90
elif fx==0 and fy<0:
    angle=270
elif fx>0 and fy==0:
    angle = 0
else:
    angle = 180



print()
print(f'The mangnitude of the force is {force:.1f} lbs.')
print(f'The angle of the Force is {angle:.1f} degrees.\n')
