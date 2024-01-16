"""
Jacob Hildebrand
3/25/23
Lsn34-int_equation_with_error.py
"""
import numpy as np

#define function to find integral of
def my_fun(x):
    return 2*x**3 + 4*x**2 + 5*x + 7

#define function to find true integral value
def true_integral_value(xl, xu):
    integral = ((2*(xu**4))/4 + (4*(xu**3))/3 + (5*(xu**2))/2 + 7*xu) - ((2*(xl**4))/4 + (4*(xl**3))/3 + (5*(xl**2))/2 + 7*xl)
    return integral

#introduce program
print(f"\nThis program approximates and calculates the true value and error of the")
print(f"integral of the equation stored in the 'my_fun' function\n")

#set up
low_limit = 0
up_limit = 5
delta = 0.2
x = np.arange(low_limit,up_limit+delta,delta)
if x[-1] > up_limit:
    x[-1] = up_limit
print(f"Integration limits: {low_limit} to {up_limit}, step size: {delta}\n")

#Approx. using trapezoidal method
area_total = 0
for i in range(len(x)-1):
    trap_area = (x[i+1]-x[i])*(my_fun(x[i])+my_fun(x[i+1]))/2
    area_total += trap_area

#calculate true value of the integral and error
true_value = true_integral_value(low_limit, up_limit)
true_relative_error = abs((true_value - area_total) / true_value) * 100

#display results
print(f"Approximate value of the integral: {area_total:.3f}")
print(f"True value of the integral: {true_value:.3f}")
print(f"True relative error: {true_relative_error:.3f}%")
