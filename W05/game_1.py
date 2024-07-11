print("Welcome to the Adventure Game!")
print("You find yourself in a dark forest.")
print("In front of you are two items: a MATCH and a FLASHLIGHT.")

choice1 = input("Which one do you want to pick up? ").lower()

if choice1 == "match":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated.")
    print("You see a large grizzly bear, and then the match burns out.")
    
    choice2 = input("Do you want to RUN, or HIDE behind a tree? ").lower()
    
    if choice2 == "run":
        print("You start running as fast as you can.")
        print("You hear the bear chasing after you.")
        print("After a while, you can no longer hear the bear.")
        print("You stop to catch your breath and realize you are lost.")
        print("Game Over!")
    elif choice2 == "hide":
        print("You quickly hide behind a nearby tree.")
        print("You hear the bear's heavy breathing and footsteps.")
        print("The bear doesn't seem to notice you and walks away.")
        print("Congratulations! You survived the encounter!")
    else:
        print("Invalid choice. Game Over!")

elif choice1 == "flashlight":
    print("You pick up the flashlight and turn it on.")
    print("You see the pathway lit up in front of you, but you thought you also heard something off to the side.")
    
    choice3 = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ").lower()
    
    if choice3 == "follow":
        print("You follow the path and eventually reach a small clearing.")
        print("In the clearing, you find an old abandoned cabin.")
        print("You cautiously approach the cabin.")
        print("To be continued...")
    elif choice3 == "look":
        print("You look into the trees and see a pair of glowing eyes staring back at you.")
        print("You freeze in fear, unsure of what to do.")
        print("Suddenly, the creature lunges at you.")
        print("Game Over!")
    else:
        print("Invalid choice. Game Over!")

else:
    print("Invalid choice. Game Over!")