print("Welcome to the Haunted Mansion Adventure!")
print("You find yourself standing in front of an old, abandoned mansion.")
print("Do you want to ENTER the mansion or LEAVE and go home?")

choice1 = input("> ").lower()

if choice1 == "enter":
    print("\nYou step inside the mansion and the door closes behind you.")
    print("You hear strange noises coming from upstairs and the basement.")
    print("Do you want to INVESTIGATE the UPSTAIRS, EXPLORE the BASEMENT, or try to OPEN the DOOR?")
    
    choice2 = input("> ").lower()
    
    if choice2 == "upstairs":
        print("\nYou cautiously climb the creaky stairs and reach the second floor.")
        print("You see a dimly lit hallway with multiple doors.")
        print("Do you want to ENTER the FIRST door, the SECOND door, or GO back downstairs?")
        
        choice3 = input("> ").lower()
        
        if choice3 == "first":
            print("\nYou enter the first door and find a ghost!")
            print("The ghost chases you, and you barely escape the mansion.")
            print("Congratulations! You survived the haunted mansion!")
        elif choice3 == "second":
            print("\nYou enter the second door and find a treasure chest filled with gold!")
            print("You take the treasure and safely exit the mansion.")
            print("Congratulations! You're rich!")
        elif choice3 == "go":
            print("\nYou decide to go back downstairs, but the ghost is waiting for you!")
            print("You become trapped in the mansion forever.")
            print("Game Over!")
        else:
            print("\nInvalid choice. The ghost catches you off guard!")
            print("Game Over!")
    
    elif choice2 == "basement":
        print("\nYou descend into the dark basement, feeling a chill run down your spine.")
        print("You see a rusty door and hear whispers coming from behind it.")
        print("Do you want to OPEN the door or GO back upstairs?")
        
        choice3 = input("> ").lower()
        
        if choice3 == "open":
            print("\nYou open the door and find a portal to another dimension!")
            print("You step through the portal and find yourself in a magical world.")
            print("Congratulations! You discovered a new realm!")
        elif choice3 == "go":
            print("\nYou decide to go back upstairs, but the stairs collapse!")
            print("You become trapped in the basement forever.")
            print("Game Over!")
        else:
            print("\nInvalid choice. The whispers intensify, and you lose your sanity!")
            print("Game Over!")
    
    elif choice2 == "open":
        print("\nYou try to open the door, but it's locked from the outside.")
        print("You hear footsteps approaching from behind...")
        print("Game Over!")
    
    else:
        print("\nInvalid choice. The mansion consumes your soul!")
        print("Game Over!")

elif choice1 == "leave":
    print("\nYou decide to leave the mansion and return home.")
    print("As you walk away, you hear a sinister laugh coming from the mansion.")
    print("You can't help but feel that you made the right choice.")
    print("Game Over!")

else:
    print("\nInvalid choice. Your indecision costs you dearly!")
    print("Game Over!")