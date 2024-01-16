#Lsn28-trap_rule.py
#Approximate the integral of an equation
#using the trapeziodal rule

#Store the equation in a Python function
def my_fun(x):
    value_of_equation = 3*x**2 + 2*x + 1
    return value_of_equation

#Integrate the equation from 0 to 5

#Single trapezoid
trap_area  = (5-0)*(my_fun(0)+my_fun(5))/2
print(f'\nUsing one trapezoid the integral is approx. {trap_area:.1f}')

#Two traps
trap1_area = (2-0)*(my_fun(0)+my_fun(2))/2
trap2_area = (4-2)*(my_fun(2)+my_fun(4))/2
total_area = trap1_area+trap2_area
print(f'\nUsing 2 trapezoid the integral is approx. {total_area:.1f}\n')
