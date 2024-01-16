import math

num = int(input("What integer do you want to find the factorial of? "))

# Calculate factorial using for loop
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("\nUsing a for loop:")
print(f"The factorial of {num} is {factorial}.")

# Calculate factorial using math library
math_factorial = math.factorial(num)
print("\nUsing the built-in function from the math library:")
print(f"The factorial of {num} is {math_factorial}.")