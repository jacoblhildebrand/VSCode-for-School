import random

def generate_hint(secret_word, guess):
    hint = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess[i]:
            hint += secret_word[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += "_"
    return hint

def main():
    print("Welcome to the word guessing game!")

    # List of secret words
    secret_words = ["mosiah", "moroni",  "temple", "jesus", "grace", "serve", "ether", "nephi", "alma", "helaman", "mormon", "omni", "lehi", "prayer", "laman", "lemuel", "jacob", "enos", "angel", "plates", "jarom", "spirit", "save"  ]

    # Select a random word
    secret_word = random.choice(secret_words)

    guesses = 0
    correct = False

    while not correct:
        print("\n", "_" * len(secret_word))
        guess = input("\nWhat is your guess? ").lower()
        guesses += 1

        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            continue

        if guess == secret_word:
            correct = True
            print("Congratulations! You guessed it!")
            print("It took you", guesses, "guesses.")
        else:
            print("Your guess was not correct.")
            print("Hint:", generate_hint(secret_word, guess))

if __name__ == "__main__":
    main()