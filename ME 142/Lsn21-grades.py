"""
Lsn21-grades
Name: Jacob Hildebrand
Date: 2/23/2023
Purpose: Given a score what is the grade
"""
#input
score = float(input('What is your score? '))

#Display grade
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'less than C'
#print results

print("your grade is " + grade)
print()


