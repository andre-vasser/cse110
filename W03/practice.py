# ask user how many friends is going on the activity
q_friends = int(input("How many frieds are coming to the activity? "))
# Number of seats in each vehicle
num_seats = int(input("How many spots by vehicle? "))
# Calculate and print the quantity of vehicles needed
num_vehicles = q_friends // num_seats
print(f'You need {num_vehicles} vehicles')
# Calculate and Print The number of loaded vehicles
real_vehicles = num_vehicles // num_seats 
print(f'You will need {real_vehicles} vehicles')
# Calculate and print the number of remaining frieds
remaining_frieds = real_vehicles