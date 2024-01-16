import math

shape = input("Do you want to find the volume of a SPHERE or CYLINDER? ").lower()

if shape == "sphere":
    radius = float(input("What is the radius of the sphere? "))
    volume = 4/3 * math.pi * radius**3
    print("\nThe volume of the sphere is {:.2f} units cubed.".format(volume))
    
elif shape == "cylinder":
    radius = float(input("What is the radius of the cylinder? "))
    length = float(input("What is the length of the cylinder? "))
    volume = math.pi * radius**2 * length
    print("\nThe volume of the cylinder is {:.2f} units cubed.".format(volume))
    
else:
    print("\nYou did not enter a valid option.")