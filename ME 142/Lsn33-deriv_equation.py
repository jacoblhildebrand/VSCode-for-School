"""
Lsn33-deriv_equation.py
Jacob Hildebrand
3/23/23

"""
import numpy as np
import matplotlib.pyplot as plt

#Define
def fun(x):
    return 2*x**3 + 4*x**2 + 5*x +7

#define the divided difference
def forward(xi, xi_plus):
    return (fun(xi_plus) - fun(xi))/(xi_plus-xi)

def backward(xi, xi_minus):
    return (fun(xi)-fun(xi_minus))/(xi - xi_minus)

def centered(xi_plus, xi_minus):
    return (fun(xi_plus)-fun(xi_minus))/(xi_plus-xi_minus)

#approximate the derivative at a point
xi = 3.5
dx = 0.5
slope_forward = forward(xi, xi+dx)
slope_backward = backward(xi, xi-dx)
slope_centered = centered(xi+dx, xi-dx)

#print
print('\nThe forwardd difference approximation of the')
print(f'slope of the function at x = {xi} is {slope_forward}')
print('\nThe backward difference approximation of the')
print(f'slope of the function at x = {xi} is {slope_backward}')
print('\nThe centered difference approximation fo the')
print(f'slope of the function at x = {xi} is {slope_centered}')
print()

# approximate the derivative across a series of points
x = np.arange(0,5.1,0.1)
y = fun(x)

deriv = []
for i in range(len(x)):
    if i == 0:
        deriv.append(forward(x[i], x[i+1]))
    elif i == len(x)-1:
        deriv.append(backward(x[i], x[i-1]))
    else:
        deriv.append(centered(x[i+1], x[i-1]))

#print

for i in range(len(x)):
    print(f'{x[i]:3.1f} {y[i]:8.3f} {deriv[i]:2.7f}')

#plot
plt.plot(x,y,label = 'Equation f(x)')
plt.grid(True)
plt.plot(x,deriv,label = "Derivative f'(x)")
plt.legend(loc = "lower right")
plt.xlabel('x')
plt.title('Plot of Equation and Derivative')
plt.xlim(0,6)
plt.ylim(0,450)
plt.show()