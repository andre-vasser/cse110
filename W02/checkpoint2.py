# Input the number of entries
num_entries = int(input("How many entries do you want to make? "))

# Initialize a list to store the entries
entries = []
# Loop to get input for each entry
for i in range(num_entries):
    first_name = input("What's your First name? ")
    last_name = input("What's your last name? ")
    entries.append((first_name, last_name))  # Store the entries as tuples
    
# Show the names
print("Complete names:")
for first_name, last_name in entries:
    print(f"{last_name}, {first_name}")