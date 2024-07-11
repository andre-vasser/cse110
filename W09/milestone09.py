# Initialize an empty shopping cart list
shopping_cart = []

# Start an infinite loop to keep the program running until the user chooses to quit
while True:
    # Display the menu options
    print("\nWelcome to the Shopping Cart Program!")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    # Get the user's choice
    choice = input("Please enter an action: ")
    
    # Handle the user's choice
    if choice == "1":
        # Add a new item to the shopping cart
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        print(f"'{item}' has been added to the cart.")
    
    elif choice == "2":
        # Display the contents of the shopping cart
        print("The contents of the shopping cart are:")
        for index, item in enumerate(shopping_cart):
            print(f"{index + 1}. {item}")
    
    elif choice == "3":
        # Remove an item from the shopping cart
        if len(shopping_cart) > 0:
            print("The contents of the shopping cart are:")
            for index, item in enumerate(shopping_cart):
                print(f"{index + 1}. {item}")
            
            item_index = int(input("Which item would you like to remove? ")) - 1
            
            if 0 <= item_index < len(shopping_cart):
                removed_item = shopping_cart.pop(item_index)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Sorry, that is not a valid item number.")
        else:
            print("The shopping cart is empty.")
    
    elif choice == "4":
        # Compute the total price of the items in the shopping cart (not implemented yet)
        print("Compute total feature is not available in this milestone.")
    
    elif choice == "5":
        # Quit the program
        print("Thank you. Goodbye.")
        break
    
    else:
        # Handle invalid options
        print("Invalid option. Please try again.")
