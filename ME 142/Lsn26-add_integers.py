num = int(input("Add integers from 1 up to and including what integer? "))
sum = 0

for i in range(1, num+1):
    sum += i

print("The sum of all integers from 1 up to and including", num, "is", sum, ".")