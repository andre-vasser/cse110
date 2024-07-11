age = int(input("Whats your age? "))
height = float(input("Whats your height? "))
rider = input("Is there another rider? ")

if rider =='yes':
    age_2 = float(input("Whats your age? "))
    height_2 = int(input("Whats your height "))
    if height >= 36 and age >= 12:
   
        if height_2 >= 36 and age_2 >= 12:
            print ("Welcome to the ride. Please be safe and have fun!")
        else:
            print ("Sorry, you may not ride.")
    elif height_2 >= 36 and age_2 >= 12:
        print ("Welcome to the ride. Please be safe and have fun!")
    else:
        print("Sorry, you may not ride.")  
else:
    if height >= 62 and age >= 18:
        print("Welcome to the ride. Please be safe and have fun!")  
    else:
        print("Sorry, you may not ride.")

        

    