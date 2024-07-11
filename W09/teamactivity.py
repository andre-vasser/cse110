number_lists = []
number = input("Enter a list of numbers, type 0 when finished. ")
while number != "0":
    number_lists.append(number)
    number = input(f"Enter the number: {number} ")

print("Your friends are: ")
for friend in friends:
    print(friend)
    

