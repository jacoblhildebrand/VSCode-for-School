"""
Bisection
Jacob Hildebrand
3/18/2023
use bisection to find roots of equations
"""
import math

#define
def f(x):
    return 2* x**3 -15*math.sqrt(x)

#bisection
def bisect(xl,xu,loops=3):
    print()
    xrt=xl
    for i in range(loops):
        xrt_old=xrt
        xrt=(xl+xu)/2
        err = abs((xrt-xrt_old)/xrt)*100
        print(f'Iter: {(i+1):2.0f}  x-root: {(xrt):.6f}  error:{err:.6f}')
        if f(xl) * f(xrt) < 0:
            xu = xrt
        else:
            xl =xrt
    return xrt,err
    
#et up values
x_lower = 2
x_upper = 3
num_loops = 3

#check for good bracket then call bisections
if f(x_lower) * f(x_upper) > 0:
    print('\nYour interval does not bracket the root.\n')
else:
    root, error = bisect(x_lower,x_upper,num_loops)
    print(f'\nAfter {num_loops} iterations the final')
    print(f'estimate of the root is {root:.6f}')
    print(f'With a relative error of {error:.6f} %\n')