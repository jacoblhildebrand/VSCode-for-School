import numpy as np

print("Welcome to the linear Equations Tool!\n")

# Get the number of equations and unknowns
num_equations = int(input("How many equations and how many unknowns are there? "))

# Initialize the A matrix to zeros
A = np.zeros((num_equations, num_equations))

# Get the A matrix values
for i in range(num_equations):
    print(f"\n[A] matrix values for row {i+1}")
    for j in range(num_equations):
        A[i,j] = float(input(f"Column {j+1}: "))

# Check if A is singular
if np.linalg.det(A) == 0:
    print("\nThe A matrix is singular so the system cannot be solved!")
else:
    # Get the b vector values
    b = np.zeros(num_equations)
    for i in range(num_equations):
        b[i] = float(input(f"\n[b] vector values for row {i+1}: "))

    # Solve the system of equations
    x = np.linalg.solve(A, b)

    # Print the A matrix, b vector, and solution
    print("\nA Matrix:")
    print(A)
    print("\nb Vector:")
    print(b)
    print("\nx Values:")
    for i in range(num_equations):
        print(f"x{i+1} = {x[i]: .3f}")