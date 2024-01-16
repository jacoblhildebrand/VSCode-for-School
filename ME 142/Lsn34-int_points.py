"""
Jacob Hildebrand
3/25/23
Lsn34-int_points.py
"""



import numpy as np

#introduce program
print('\nThis program approximates the integrals')
print("using discrete data points\n")

#set up
time = [0,1,2.5,3,4.5,6]
velocity = [0,1,1.5,2,3,4]

#isplay ot user
print(f'The time values are {time}')
print(f'The velocity values are {velocity}')

#approximate
area_total = 0
for i in range(len(time)-1):
    trap_area = (time[i+1]-time[i])*(velocity[i]+velocity[i+1])/2
    area_total += trap_area

#display
print(f'The value of the integral is {area_total:.3f}')