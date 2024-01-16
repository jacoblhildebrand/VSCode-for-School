import numpy as np

def f(x):
    return 4*x**2 - 12*x + np.exp(0.5*x)

def f_prime(x):
    return 8*x - 12 + 0.5*np.exp(0.5*x)

def divided_diff_quotient(x, y, i, j):
    if j == i:
        return y[i]
    elif j == i+1:
        return (y[j] - y[i]) / (x[j] - x[i])
    else:
        return (divided_diff_quotient(x, y, i+1, j) - divided_diff_quotient(x, y, i, j-1)) / (x[j] - x[i])

x_values = np.arange(0, 5.1, 0.1)
f_values = f(x_values)
f_prime_approx = []
f_prime_true = f_prime(x_values)

for i in range(len(x_values)):
    if i == 0:
        f_prime_approx.append(divided_diff_quotient(x_values, f_values, i, i+1))
    elif i == len(x_values) - 1:
        f_prime_approx.append(divided_diff_quotient(x_values, f_values, i-1, i))
    else:
        f_prime_approx.append(divided_diff_quotient(x_values, f_values, i-1, i+1))

print(" x      f(x)     f'(x)_approx     f'(x)_true")
print("{:<5}  {:<8.3f}  {:<15.2f}  {:<15.2f}".format(x_values[0], f_values[0], f_prime_approx[0], f_prime_true[0]))

for i in range(1, len(x_values)):
    print("{:<5}  {:<8.3f}  {:<15.2f}  {:<15.2f}".format(x_values[i], f_values[i], f_prime_approx[i], f_prime_true[i]))
