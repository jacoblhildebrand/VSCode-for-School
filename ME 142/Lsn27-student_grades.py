# initialize empty lists for students and grades
students = []
grades = []

# get input from user and build the lists
print('Enter student names and their grades.\n')
name = input("Enter student name ('end' to quit): ").capitalize()
while name != "end":
    grade = int(input("Enter grade for {}: ".format(name)))
    students.append(name)
    grades.append(grade)
    name = input("Enter student name ('end' to quit): ")

# calculate summary statistics
avg_grade = sum(grades) / len(grades)
max_grade = max(grades)
max_student = students[grades.index(max_grade)]
min_grade = min(grades)
min_student = students[grades.index(min_grade)]

# display results
print("\nStudent     Grades")
for i in range(len(students)):
    print("{:<12} {}".format(students[i], grades[i]))

print("\nThe average grade is {:.1f}".format(avg_grade))
print("{} has the highest grade of {}".format(max_student, max_grade))
print("{} has the lowest grade of {}".format(min_student, min_grade))