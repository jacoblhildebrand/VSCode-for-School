#Ask user for name
name = input ("Hello! What is your name?")
#Display name and ask how their day was
day = input("Hi, "+name+"! How was your day?")
#Output response
if day.lower() in ["good", "great", "wonderful"]:
    print("Good! I am glad you're having a good day, "+name+".")
else:
    print("I'm sorry you're not having a good day, "+name+".") 