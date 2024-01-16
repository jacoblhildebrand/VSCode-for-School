"""
File: Lsn18-ID_card
Jacob Hildebrand
02/16/2023
Purpose: Show information given for an ID card
"""
# user input
first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID number: ")

# ID card string
id_card = "-------------------------------------\n"
id_card += last_name.upper() + ", " + first_name.capitalize() + "\n"
id_card += job_title.title() + "\n"
id_card += "ID: " + id_number + "\n\n"
id_card += email.lower() + "\n"
id_card += phone_number + "\n"
id_card += "-------------------------------------"

# Print
print("The ID Card is:\n" + id_card)