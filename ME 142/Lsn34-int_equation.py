"""
Jacob Hildebrand
3/25/23
Lsn34-int_equation.py
"""
import numpy as np

#define function to find integral of
def my_fun(x):
    return 2*x**3 + 4*x**2 + 5*x + 7

#introduce program
print('\nThis program approximates the integral of the')
print("equation that is stored in the 'my_fun' function\n")

#set up
low_limit = 0
up_limit = 4
delta = 0.3
x = np.arange(low_limit,up_limit+delta,delta)
if x[-1] > up_limit:
    x[-1] = up_limit
print(x)

#Approx. using trapezoidal method
area_total = 0
for i in range(len(x)-1):
    trap_area = (x[i+1]-x[i])*(my_fun(x[i])+my_fun(x[i+1]))/2
    area_total += trap_area

#display
print(f'The value of the integral is {area_total:.3f}')