import random

# List of possible secret words
secret_words = ["nephi", "mosiah", "helaman", "moroni", "alma", "ether", "helaman"]

# Choose a random word from the list
secret_word = random.choice(secret_words)
secret_word_length = len(secret_word)

# Prepare the initial hint
current_hint = ["_"] * secret_word_length

print("Welcome to the word guessing game!\n")
print("Guess a prophet name from the book of Mormon")

# Display initial hint
print(f"Your hint is: {' '.join(current_hint)}")

# Track number of guesses
num_guesses = 0

# Game loop
while True:
    print()
    guess = input("What is your guess? ").lower()  # Convert guess to lowercase

    # Validate the length of the guess
    if len(guess) != secret_word_length:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        num_guesses += 1
        continue

    num_guesses += 1
    
    # Check if the guess is correct
    if guess == secret_word:
        print(f"Congratulations! You guessed it!\nIt took you {num_guesses} guesses.")
        break

    # Generate hint for the current guess
    hint = []
    for i in range(secret_word_length):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())
        elif guess[i] in secret_word:
            hint.append(guess[i])
        else:
            hint.append("_")
    
    # Display hint
    print(f"Your hint is: {' '.join(hint)}")
