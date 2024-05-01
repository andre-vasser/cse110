# Get information
first_name = input('Enter the first name: ')
last_name = input('Enter the last name: ')
email = input('Enter email address: ')
phone_number = input('Enter the phone number: ')
job_title = input('Enter the Job Title: ')
id_number = input('Enter the Id Number: ')
color_hair = input('Enter color hair: ')
color_eyes = input('Enter color eyes: ')
start_month = input('Enter Start Month: ')
status = input('What\'s your training status?: ')

# Print Id Card
print('The Id Card is:')
print('-' * 40)
print(f'{last_name.ljust(15)}, {first_name.ljust(15)}')  # Align last and first names
print(f'{job_title.ljust(30)}')  # Align job title
print(f'{id_number.ljust(30)}\n')  # Align id number
print(f'{email.ljust(30)}')  # Align email
print(f'{phone_number.ljust(30)}\n')  # Align phone number
print(f'Hair: {color_hair.ljust(10)} Eyes: {color_eyes.ljust(10)}')  # Align hair and eye colors
print(f'Month: {start_month.ljust(10)} Training: {status.ljust(20)}')  # Align start month and training status
print('-' * 40)