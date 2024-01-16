# Ask the user for the number of students
num_students = int(input("How many students do you need to enter grades for? "))

# Initialize lists for student names and grades
students = []
grades = []

# Get the names and grades of the students from the user
for i in range(num_students):
    name = input(f"Name of student #{i+1}: ")
    grade = int(input(f"Grade for {name.capitalize()}: "))
    students.append(name.capitalize())
    grades.append(grade)

# Calculate the average grade, maximum grade, and minimum grade
average_grade = sum(grades) / len(grades)
max_grade = max(grades)
max_student = students[grades.index(max_grade)]
min_grade = min(grades)
min_student = students[grades.index(min_grade)]

# Print the student names and grades, along with the average, maximum, and minimum grades
print("\nStudent\t\tGrades")
for i in range(num_students):
    print(f"{students[i]:<10}\t{grades[i]:>3}")
print(f"\nThe average grade is {average_grade:.1f}")
print(f"{max_student} had the highest grade of {max_grade}")
print(f"{min_student} had the lowest grade of {min_grade}")