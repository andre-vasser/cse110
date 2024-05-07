import math
lenght_cm = float(input("Enter a lenght value in centimeters : "))

lenght_m = lenght_cm / 100

square_area_cm2 = (lenght_cm ** 2)
square_area_m2 = (lenght_m ** 2)
print((f"Area of a square with side lenght {lenght_cm}cm is: {square_area_cm2:.2f} and {lenght_m}is: {square_area_m2:.2f}"))

circle_area_cm2 = math.pi * (lenght_cm ** 2)
circle_area_m2 = math.pi * (lenght_m ** 2)
print (f'Area of cirle radius is {circle_area_cm2}cm^2 and {circle_area_m2:.2f}m2')

width_cm = float(input("Enter the width in cm: "))
width_m = lenght_cm ** width_cm
rectangle_area_cm = lenght_cm * width_cm
rectangle_area_m = lenght_m * width_m
print(f"area of a rectangle are {rectangle_area_cm:.2f}cm2 and {rectangle_area_m:.2f}m")
