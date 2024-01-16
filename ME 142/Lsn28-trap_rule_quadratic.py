#Lsn28-trap_rule_quadratic.py

# Store the equation in a Python function
def my_fun(x):
    value_of_equation = -2*x**2 + 10*x + 18
    return value_of_equation

# Integrate the equation from 0 to 4

# Single trapezoid
trap_area = (4-0)*(my_fun(0)+my_fun(4))/2
print(f'Using 1 trapezoid, the integral is approximately {trap_area:.1f}')

# Two traps
trap1_area = (2-0)*(my_fun(0)+my_fun(2))/2
trap2_area = (4-2)*(my_fun(2)+my_fun(4))/2
total_area = trap1_area + trap2_area
print(f'Using 2 trapezoids, the integral is approximately {total_area:.1f}')