import math
square_side = int(input("What is the length of a side of the square? "))
print ("The area of the square is:",square_side^2,)

rect_length = int(input("What is the length of the rectangle? "))
rect_width = int(input("What is the width of the rectangle? "))
print ("The are of the rectangle is:",rect_length*rect_width,)

radius = float(input("What is the radius of the circle? "))
area_c = math.pi*radius**2
print ("The area of the circle is: ",area_c,"")