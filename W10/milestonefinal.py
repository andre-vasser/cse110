# Initialize the shopping cart lists
cart_items = []
cart_prices = []

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
        price = float(input(f"What is the price of '{item}'? "))
        cart_items.append(item)
        cart_prices.append(price)
        print(f"'{item}' has been added to the cart.")
        
    elif choice == "2":
        # View cart
        print("The contents of the shopping cart are:")
        for i in range(len(cart_items)):
            print(f"{i + 1}. {cart_items[i]} - ${cart_prices[i]:.2f}")
            
    elif choice == "3":
        # Remove item from the cart
        item_number = int(input("Which item would you like to remove? "))
        if 1 <= item_number <= len(cart_items):
            index = item_number - 1
            removed_item = cart_items.pop(index)
            removed_price = cart_prices.pop(index)
            print(f"Item '{removed_item}' removed.")
        else:
            print("Sorry, that is not a valid item number.")
            
    elif choice == "4":
        # Compute total price of items in the cart
        total = sum(cart_prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
        
    elif choice == "5":
        # Quit the program
        print("Thank you. Goodbye.")
        break
    
    else:
        print("Invalid option, please try again.")
