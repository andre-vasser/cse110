import math

print ("Welcome to the velocity calculator. Please enter the following:")

mass = float(input("Mass in Kg: "))
gravity = float(input("Gravity(in m/s^2, 9.8 for Earth, 24 for Jupter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sectional_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

inner_value = (1/2) * density * cross_sectional_area * drag_constant
velocity_terminal = math.sqrt(mass * gravity / drag_constant) * (1 - math.exp((-math.sqrt(mass*drag_constant * gravity) /mass) * time)) 

print ("Welcome to the velocity calculator. Please enter the following:")
print (f"Mass in Kg: {mass}")
print (f"Gravity(in m/s^2, 9.8 for Earth, 24 for Jupter): {gravity:.1f}")
print (f"Time (in seconds): {time}")
print (f"Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): {density:.1f}")
print (f"Cross sectional area (in m^2): {cross_sectional_area:.2f}")
print (f"Drag constant (0.5 for sphere, 1.1 for cylinder): {drag_constant:.1f}")

print (f"The inner value of c is: {inner_value:.3f}")
print (f"The velocity after 10.0 seconds is: {velocity_terminal:.3f} m/s")