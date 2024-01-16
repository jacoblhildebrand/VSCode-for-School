"""
Lsn28-calculate_areas
Jacob Hildebrand
3/11/2023
Create functions to calculate the area of basic shapes
"""
import math

#function to compute area of square
def compute_area_square(length):
    area_square = length**2
    return area_square

#function to compute area of rectangle
def compute_area_rectangle(length1,length2):
    area_rectangle = length1*length2
    return area_rectangle

#function to compute area of circle
def compute_area_circle(radius):
    area_circle = math.pi*radius**2
    return area_circle
print()
shape = input("What shape do you want the area of ('square', 'recatngle', 'circle')?").lower()
if shape=='square':
    length = float(input('What is the lenght of the square? '))
    area = compute_area_square(length)
    print(f'The area of the square is {area:.2f}\n')
elif shape == 'rectangle':
    length1 = float(input('What is the lenght of the first sid eof the recatangle? '))
    length2 = float(input('What is the lenght of the second sid eof the recatangle? '))
    area = compute_area_rectangle(length1,length2)
    print(f'The area of the rectangle is {area:.2f}\n')
elif shape == 'circle':
    radius = float(input('What is the radius of the cirlce? '))
    area = compute_area_circle(radius)
    print(f'The area of the cirlce is {area:.2f}\n')
else:
    print('Invalid Entry\n')