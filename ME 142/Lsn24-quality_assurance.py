import math
import numpy as np

# Create arrays for the measured dimensions
length1 = np.array([12, 10.59, 10.7, 10.58, 10.55, 10.57, 10.63, 10.45, 10.58, 10.47])
length2 = np.array([3.15, 3.27, 3.3, 3.18, 3.23, 3.33, 3.25, 3.27, 3.18, 3.19])
large_diam = np.array([1.01, 0.97, 1, 1.06, 1.05, 0.93, 1.02, 1.11, 0.92, 0.93])
small_diam = np.array([0.53, 0.47, 0.47, 0.46, 0.5, 0.51, 0.49, 0.46, 0.45, 0.51])

# Calculate the volume values
radius1 = large_diam / 2
radius2 = small_diam / 2
area1 = math.pi * radius1**2
area2 = math.pi* radius2**2
volume = (area1*(length1-length2))+(area2*length2)

# Calculate summary statistics for the volumes
avg_volume = np.mean(volume)
std_volume = np.std(volume)
max_volume = np.max(volume)
min_volume = np.min(volume)

# Display the volume values and summary statistics
print("The volume values are", volume)
print("The average of the volumes is {:.2f}.".format(avg_volume))
print("The standard deviation of the volumes is {:.2f}.".format(std_volume))
print("The maximum of the volumes is {:.2f}.".format(max_volume))
print("The minimum of the volumes is {:.2f}.".format(min_volume))