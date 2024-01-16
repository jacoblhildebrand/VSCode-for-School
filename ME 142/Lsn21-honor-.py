# get user input
gpa = float(input("What is your GPA? "))
essay = input("What is your essay category? ")

# check if user is eligible for honor roll
if gpa >= 3.5 and (essay.lower() == "excellent" or essay.lower() == "very good"):
    print("Congratulations! You can graduate with honors!")
else:
    print("You are not eligible to graduate with honors.")