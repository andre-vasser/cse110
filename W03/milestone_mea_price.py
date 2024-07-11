# Ask the user for meal prices
child_meal_price = float(input("Enter the price of a child's meal: "))
adult_meal_price = float(input("Enter the price of an adult's meal: "))

# Ask the user for the number of people
num_children = int(input("Enter the number of children: "))
num_adults = int(input("Enter the number of adults: "))

# Ask the user for the sales tax rate
sales_tax_rate = float(input("Enter the sales tax rate (e.g., 0.06 for 6%): "))

# Calculate the subtotal
subtotal = (num_children * child_meal_price) + (num_adults * adult_meal_price)
print(f"Subtotal: ${subtotal:.2f}")

# Calculate the sales tax
sales_tax = subtotal * sales_tax_rate
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate the total
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

# Ask the user for the payment amount
payment = float(input("Enter the payment amount: "))

# Calculate the change
change = payment - total
print(f"Change: ${change:.2f}")