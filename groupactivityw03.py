import math
l_side = int(input("What\'s the lenght of a side of the square?"))
a_square = l_side ** 2
print(f"The area of the square is: {a_square}")

l_rectangle = float(input("What\'s the length of the rectangle? "))
w_rectangle = float(input("What\'s the width of the rectangle? "))
r_area = l_rectangle * w_rectangle
print(f"The area of the rectangle is: {r_area}")

radius = float(input("What\'s the radius of the circle? "))
a_circle = math.pi * radius ** 2
print (f'The area of the circle is: {a_circle:.2f}')


a_square = l_side ** 2
print(f"The area of square with side lenght is: {a_square}")
c_area = math.pi * (l_side ** 2)
print(f"The area of the circle with radius is: {c_area:.2f}")
c_volume = l_side ** 3
print(f"The volume of a cube with {l_side} side lenght is: {c_volume}")
s_volume = (4/3) *math.pi * (l_side ** 3)


