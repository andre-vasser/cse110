secret_word = "mosiah"
num_guesses = 0
guess = ""

print("Welcome to the word guessing game!")

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    num_guesses += 1
    print("Your guess was not correct.")

print("Congratulations! You guessed it!")
print(f"It took you {num_guesses} guesses.")