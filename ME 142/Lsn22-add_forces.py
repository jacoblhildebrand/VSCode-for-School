import math

print("This program will add two forces together")
print("and display the resultant force and angle.\n")

# get input values from the user
F1_mag = float(input("What is the magnitude of the first force (in lbs)? "))
F1_deg = float(input("What is the angle of the first force (in degrees)? "))
F2_mag = float(input("What is the magnitude of the second force (in lbs)? "))
F2_deg = float(input("What is the angle of the second force (in degrees)? "))

# convert angles to radians
F1_rad = math.radians(F1_deg)
F2_rad = math.radians(F2_deg)

# calculate x and y components of each force
F1x = F1_mag * math.cos(F1_rad)
F1y = F1_mag * math.sin(F1_rad)
F2x = F2_mag * math.cos(F2_rad)
F2y = F2_mag * math.sin(F2_rad)

# add x and y components of the forces to get x and y components of the resultant force
Fx = F1x + F2x
Fy = F1y + F2y

# calculate magnitude and angle of the resultant force
F_res_mag = math.sqrt(Fx**2 + Fy**2)
theta_res = math.degrees(math.atan2(Fy, Fx))

# adjust angle to range of 0 to 360 degrees
if theta_res < 0:
    theta_res += 360

# print the results
print("\nThe magnitude of the resultant force is", round(F_res_mag, 1), "lbs.")
print("The angle of the resultant force is", round(theta_res, 1), "degrees.")