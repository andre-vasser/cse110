print("Welcome to the Shopping Cart Program!")

cart = []

while True:
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Quit")
    print("Please enter an action: ", end='')
    
    action = input()
    
    if action == '1':
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to the cart.")
    elif action == '2':
        if not cart:
            print("The cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for item in cart:
                print(item)
    elif action == '3':
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")


print("Welcome to the Shopping Cart Program!")

cart = []
prices = []

while True:
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print("Please enter an action: ", end='')
    
    action = input()
    
    if action == '1':
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        cart.append(item)
        prices.append(price)
        print(f"'{item}' has been added to the cart.")
    
    elif action == '2':
        if not cart:
            print("The cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for index in range(len(cart)):
                print(f"{index + 1}. {cart[index]} - ${prices[index]:.2f}")
    
    elif action == '3':
        if not cart:
            print("The cart is empty, no items to remove.")
        else:
            index = int(input("Which item would you like to remove? ")) - 1
            if 0 <= index < len(cart):
                removed_item = cart.pop(index)
                prices.pop(index)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Sorry, that is not a valid item number.")
    
    elif action == '4':
        if not cart:
            print("The cart is empty, no total to compute.")
        else:
            total = sum(prices)
            print(f"The total price of the items in the shopping cart is ${total:.2f}")
    
    elif action == '5':
        print("Thank you. Goodbye.")
        break
    
    else:
        print("Invalid choice. Please try again.")
