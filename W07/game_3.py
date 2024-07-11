print("You are going in an adventure.")
print("Be prepared for each kind of terrain")
print("Choice between SEA, MOUNTAIN or FOREST")

choice1 = input("> ").lower()

if choice1 == "SEA":
    print("SEA: You need to survive for 3 days, chose the necessary equipments")
    print("Choose one option that most important in this terrain")
    print("WATER, HAT, SUNGLASSES")
    
    choice2 = input("> ").lower()
    
    if choice2 == "WATER":
        print("GOOD OPTION. YOU WILL SURVIVE!")
    else:
        print("SORRY. YOU WILL NOT SURVIVE!")
    
