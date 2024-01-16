"""
Jacob Hildebrand
Lsn23-geometry
3/2/23
Do geometry math
"""
import math

print("Do you want to calculate an AREA or a VOLUME?")
calculation_type = input("> ")

if calculation_type.lower() == "area":
    print("Do you want to find the area of a TRIANGLE or CIRCLE?")
    shape_type = input("> ")
    
    if shape_type.lower() == "triangle":
        print("What is the base of the triangle?")
        base = float(input("> "))
        print("What is the height of the triangle?")
        height = float(input("> "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area:.2f} units squared.")
        
    elif shape_type.lower() == "circle":
        print("What is the radius of the circle?")
        radius = float(input("> "))
        area = math.pi * radius ** 2
        print(f"The area of the circle is {area:.2f} units squared.")
        
    else:
        print("Invalid shape type. Please choose 'triangle' or 'circle'.")

elif calculation_type.lower() == "volume":
    print("Do you want to find the volume of a SPHERE or CYLINDER?")
    shape_type = input("> ")
    
    if shape_type.lower() == "sphere":
        print("What is the radius of the sphere?")
        radius = float(input("> "))
        volume = 4/3 * math.pi * radius ** 3
        print(f"The volume of the sphere is {volume:.2f} units cubed.")
        
    elif shape_type.lower() == "cylinder":
        print("What is the radius of the cylinder?")
        radius = float(input("> "))
        print("What is the length of the cylinder?")
        length = float(input("> "))
        volume = math.pi * radius ** 2 * length
        print(f"The volume of the cylinder is {volume:.2f} units cubed.")
        
    else:
        print("Invalid shape type. Please choose 'sphere' or 'cylinder'.")
        
else:
    print("Invalid calculation type. Please choose 'area' or 'volume'.")