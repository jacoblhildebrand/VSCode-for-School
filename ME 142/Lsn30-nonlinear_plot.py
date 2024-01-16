import numpy as np
import matplotlib.pyplot as plt

# Define variables
p = 1.23    # density of air (kg/m^3)
A = 0.01    # cross-sectional area of the object (m^2)
C = 0.47      # drag coefficient
data = np.array([[0, 0], [3, 0.03], [8, 0.12], [12, 0.35], [15, 0.7], [20, 1.25], [23, 1.3]])

# Create a range of velocities
v = np.arange(0, 25, 0.1)

# Calculate the drag force at each velocity
Fd = 0.5 * p * A * C * v**2

# Plot the calculated drag force and the data points
plt.plot(v, Fd, label='Calculated')
plt.plot(data[:,0], data[:,1], 'o', label='Data')

# Customize the plot
plt.title('Drag Force vs Velocity')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Drag Force (N)')
plt.legend()
plt.grid(True)
plt.xlim(0, 25)
plt.ylim(0, 1.5)
plt.savefig('Lsn30-nonlinear_plot.png')
plt.show()