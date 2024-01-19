# Ask user for words
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ")
verb2 = input("Enter another verb: ")
noun = input("Enter a noun: ")
adverb = input("Enter an adverb: ")

exclamation = exclamation.capitalize()

article_noun = "an" if noun[0].lower() in ['a', 'e', 'i', 'o', 'u'] else "a"

# Display the story
story = f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. '{exclamation}!' I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb2} right in front of my family.
I then found {article_noun} {noun} and {adverb} gave it to the {animal}."
print("\nHere's the Mad Libs story:")
print(story)