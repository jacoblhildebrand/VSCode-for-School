"""
File: Greeting
Jacob Hildebrand
02/16/2023
Pupose: Greet the User
"""

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
fav_color = input('What is your favorite color? ')
print('Hello there,')
print(f'{first_name.capitalize()} {last_name.capitalize()}')
print(f'Your favorite color is {fav_color.lower()}.')
