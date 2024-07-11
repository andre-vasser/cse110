age_1 = int(input("Whats your age? "))

if age_1 <= 17 and age_1 >= 12:
    has_ticket_1 = input("Do you have a golden passport? ")
    if has_ticket_1 == 'True':
        age_1 = 18

height_1 = float(input("Whats your height?  "))

rider = input("Is there another rider? ")

if rider =='yes':
    age_2 = float(input("Whats your age? "))
    
    if age_2 <= 17 and age_2 >= 12:
        has_ticket_2 = input("Do you have a golden passport? ")
    if has_ticket_2 == 'True':
        age_2 = 18
        
    height_2 = int(input("Whats your height "))
    
if height_1 < 36 or height_2 < 36:
    print("You are not allowed to ride")
else:
    if age_1 >= 18 and height_1 >=62:
        print("You can ride")

    