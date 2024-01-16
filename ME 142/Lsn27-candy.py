print("Welcome to the small child simulator!\n")

response = "no"
count = 0

while response != "yes":
    response = input("Can I have a piece of candy? ")
    count += 1

print("\nThank you!\n")
print("I only had to ask", count, "times :-)")