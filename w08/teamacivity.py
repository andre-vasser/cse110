quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

while True:
    n = int(input("Please enter a number: "))
    
    for i, letter in enumerate(quote):
        if (i + 1) % n == 0:
            print(letter.upper(), end="")
        else:
            print(letter, end="")
    
    print()  # Print a new line after each iteration
    
    answer = input("Would you like to enter another number? ").lower()
    if answer != "yes":
        print("Goodbye")
        break