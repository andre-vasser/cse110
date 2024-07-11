number = float(input("Enter a number (Angle) between 0 and 360"))

if number == 0:
    print("N")
elif number > 0 and number < 45:
    print("NNE")
elif number == 45:
    print("NE")
elif number > 45 and number < 90:
    print("ENE")
elif number == 90:
    print("E")
elif number > 90 and number < 135:
    print ("ESE")
elif number == 135:
    print("SE")
elif number > 135 and number < 180:
    print("SSE")
elif number == 180:
    print("S")
elif number > 180 and number < 225:
    print("SSW")
elif number == 225:
    print("SW")
elif number > 225 and number < 270:
    print ("WSW")
elif number == 270:
    print ("W")
elif number > 270 and number < 315:
    print("WNW")
elif number == 315:
    print("NW")
elif number > 315 and number < 360:
    print("NNW")
elif number == 360:
    print("N")
else:
    print ("The number is not between 0 and 360")