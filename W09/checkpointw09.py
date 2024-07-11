friends = []
name = input("Type the name of a friend: ")
while name != "end":
    friends.append(name)
    name = input("Type the name of a friend (or 'end' to finish): ")

print("Your friends are: ")
for friend in friends:
    print(friend)
    

