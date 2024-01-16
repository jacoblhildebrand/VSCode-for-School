

print("This program will determine whether you made the honor roll.")
gpa = float(input("What was your Grade Point Average? "))
lowest_grade = float(input("What was your lowest grade? "))

if gpa >= 0.85 and lowest_grade >= 0.70:
    print("Congratulations! You made the honor roll.")
else:
    print("Sorry, you did not make the honor roll.")