#Lsn26-force_calculator
#Jacob Hildebrand
#3/9/2023
#



import math

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * math.pi / 180

# Function to convert radians to degrees
def radians_to_degrees(radians):
    return radians * 180 / math.pi

# Function to break a force into its x and y component forces
def force_to_components(force, angle):
    angle_radians = degrees_to_radians(angle)
    x_component = force * math.cos(angle_radians)
    y_component = force * math.sin(angle_radians)
    return x_component, y_component

# Function to combine component forces into a resultant force and angle
def force_from_components(x_component, y_component):
    magnitude = math.sqrt(x_component**2 + y_component**2)
    angle_radians = math.atan2(y_component, x_component)
    angle_degrees = 360+radians_to_degrees(angle_radians)
    return magnitude, angle_degrees

# Function to add multiple forces
def add_forces(num_forces):
    forces = []
    for i in range(num_forces):
        magnitude = float(input(f"What is the magnitude of force #{i+1} (in lbs)? "))
        angle = float(input(f"What is the angle of force #{i+1} (in degrees)? "))
        forces.append((magnitude, angle))
    
    x_components = []
    y_components = []
    for force in forces:
        x_component, y_component = force_to_components(force[0], force[1])
        x_components.append(x_component)
        y_components.append(y_component)
        
        print(f"   {len(x_components)}{' '*8}{force[0]:.1f}{' '*8}{force[1]:.1f}")
    
    x_sum = sum(x_components)
    y_sum = sum(y_components)
    
    magnitude, angle = force_from_components(x_sum, y_sum)
    print(f"\nThe magnitude of the resultant force is {magnitude:.1f} lbs.")
    print(f"The angle of the resultant force is {angle:.1f} degrees.")

# Main program
print("You may do one of the following:")
print("    1. Break a force into its x and y component forces")
print("    2. Combine component forces into a resultant force and angle")
print("    3. Add multiple forces")

option = input("Which option do you want? ")

if option == '1':
    force = float(input("What is the magnitude of the force (in lbs)? "))
    angle = float(input("What is the angle of the force (in degrees)? "))
    
    x_component, y_component = force_to_components(force, angle)
    print(f"\nThe x-component of the force is {x_component:.1f} lbs.")
    print(f"The y-component of the force is {y_component:.1f} lbs.")
    
elif option == '2':
    x_component = float(input("What is the x-component of the force (in lbs)? "))
    y_component = float(input("What is the y-component of the force (in lbs)? "))
    
    magnitude, angle = force_from_components(x_component, y_component)
    print(f"\nThe magnitude of the force is {magnitude:.1f} lbs.")
    print(f"The angle of the force is {angle:.1f} degrees.")
    
elif option == '3':
    num_forces = int(input("How many forces do you want to add? "))
    print("\nNumber    Force (lbs)    Angle (deg)")
    add_forces(num_forces)
    
else:
    print("\nYou did not enter a valid option.")
