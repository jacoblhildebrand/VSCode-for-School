import math

#define
def f(x):
    return 2* x**2 -9.5*math.sqrt(x)

#false position
def false_pos(xl,xu,loops=10):
    print()
    xrt=xl
    for i in range(loops):
        xrt_old=xrt
        xrt=xl-f(xl)*(xu-xl)/(f(xu)-f(xl))
        err = abs((xrt-xrt_old)/xrt)*100
        print(f'Iter: {i+1:2.0f}  x-root: {xrt:.6f}  error: {err:.6f}')
        if f(xl) * f(xrt) < 0:
            xu = xrt
        else:
            xl =xrt
    return xrt,err
    
#set up values
x_lower = 2.5
x_upper = 3.0
num_loops = 5

#check for good bracket then call false position
if f(x_lower) * f(x_upper) > 0:
    print('\nYour interval does not bracket the root.\n')
else:
    root, error = false_pos(x_lower,x_upper,num_loops)
    print(f'\nAfter {num_loops} iterations the final estimate of the root is {root:.6f}')
    print(f'with a relative error of {error:.6f} %\n')