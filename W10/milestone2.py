# Initialize the shopping cart list
cart = []

while True:
    # Display the menu
    print("\nWelcome to the Shopping Cart Program!")
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    # Get the user's choice
    choice = input("Please enter an action: ")
    
    if choice == "1":
        # Add item to the cart
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to the cart.")
        
    elif choice == "2":
        # View cart
        print("The contents of the shopping cart are:")
        for item in cart:
            print(item)
            
    elif choice == "5":
        # Quit the program
        print("Thank you. Goodbye.")
        break
    
    else:
        print("Invalid option, please try again.")
