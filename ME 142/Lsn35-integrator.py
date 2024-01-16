import numpy as np


def my_fun(x):
    return 2*x**3 + 4*x**2 + 5*x + 7


def calculate_trapezoidal_area(x, fx, step_size):
    area = 0
    for i in range(len(x) - 1):
        area += (fx[i] + fx[i+1]) * step_size / 2
    return area


def calculate_true_integral(lower, upper):
    xu = upper
    xl = lower
    true_value = ((2*(xu)**4)/4 + (4*(xu)**3)/3 + (5*(xu)**2)/2 + 7*xu) - ((2*(xl)**4)/4 + (4*(xl)**3)/3 + (5*(xl)**2)/2 + 7*xl)
    return true_value


def calculate_true_error(true, approx):
    return abs((true - approx) / true) * 100


print("This program approximates the integral of the equation that is stored in the 'my_fun' function.\n")

lower = float(input("What is the lower limit of integration? "))
upper = float(input("What is the upper limit of integration? "))

if upper <= lower:
    print("\nThe upper limit must be greater than the lower limit!")
else:
    step_size = float(input("\nWhat is the step size (or delta x) value? "))

    if step_size >= (upper - lower):
        print("\nThe step size must be less than the range of integration!")
    else:
        x = np.arange(lower, upper + step_size, step_size)
        fx = my_fun(x)

        if x[-1] > upper:
            x[-1] = upper

        approx_area = calculate_trapezoidal_area(x, fx, step_size)
        true_area = calculate_true_integral(lower, upper)
        true_error = calculate_true_error(true_area, approx_area)

        print("\nIntegrating the function in the 'my_fun' function from {} to {} with a step size of {} gives the following results:\n".format(lower, upper, step_size))
        print("Approximate value of the integral: {:.3f}".format(approx_area))
        print("True value of the integral: {:.3f}".format(true_area))
        print("True relative error: {:.3f} %".format(true_error))