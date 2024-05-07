'''For this assignment, you will implement a program that asks the user for a series of words and then displays the story with the user's words inserted into the appropriate places.

The program should begin by asking the user for each of the words. It should then, fill those words into the appropriate places in the story.

To begin, please use the following story:

The other day, I was really in trouble. It all started when I saw a very
[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
I could think to do was to [verb] over and over. Miraculously,
that caused it to stop, but not before it tried to [verb]
right in front of my family.'''

adjective = input("Enter one adjective: ")
animal = input("Enter the name of an animal: ")
verb = input("Enter with one verb: ")
exclamation1 = input("Enter with one exclamation: ")
verb2 = input("Enter with second verb: ")
verb3 = input("Enter with the third verb: ")

#print
print ("-" *40)
print ("Your story is:"+"\n"*3)
print ("The other day, I was really in trouble.") 
print (f"It all started when I saw a very {adjective.lower()} {animal.lower()} {verb.lower()} down the hallway.")
print (f"{exclamation1.capitalize()}! I yelled. But all I could think to do was to {verb2.lower()} over and over.")
print (f"Miraculously,that caused it to stop, but not before it tried to {verb3.lower()} right in front of my family.")

 