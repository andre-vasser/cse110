import math

print ("Welcome to the velocity calculator. Please enter the following:")

m = float(input("Enter mass (in Kg): "))
g = float(input("Enter acceleration due to gravity(9.8m/s^2 on Earth, 24m/s^2 on Jupter): "))
t = float(input("Time (in seconds): "))
p = float(input("Enter density of the fluid (1.3 kg/m^3 for air, and 1000 kg/m^3 for water): "))
A = float(input("Enter the cross secctional area of projectile (in square meters): "))
C = float(input("Enter the drag constant(0.5 for sphere, 1.1 for cylinder falling on its side)"))

c = (1/2) * p * A * C
v = math.sqrt(m/c) * (1 - math.exp((-math.sqrt(m * g * c) / m) *    t))
                      
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")
