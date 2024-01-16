import math

#define function
def f(x):
    return 2 * x**2 - 9.5 * math.sqrt(x)

#false position
def false_position(xl, xu, err_tol):
    iter = 0
    err = 100
    xrt = xl
    while err > err_tol :
        iter += 1
        xrt_old = xrt
        xrt = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
        err = abs((xrt - xrt_old) / xrt) * 100
        print(f'Iter: {iter:2.0f}  x-root: {xrt:.6f}  error: {err:.6f}')
        if f(xl) * f(xrt) < 0:
            xu = xrt
        else:
            xl = xrt
    return xrt, err, iter

#set up values
x_lower = 2.5
x_upper = 3.0
err_tol = 0.001

#check for good bracket then call false_position
if f(x_lower) * f(x_upper) > 0:
    print('\nYour interval does not bracket the root.\n')
else:
    root_value, error_value, num_iters = false_position(x_lower, x_upper, err_tol)
    print(f'\nAfter {num_iters} iterations the final')
    print(f'estimate of the root is {root_value:.6f}')
    print(f'with a relative error of {error_value:.6f} %\n')