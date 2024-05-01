#get information
first_name = input ('Enter the first name:  ').capitalize()
last_name = input ('Enter the last name:  ').upper()
email = input ('Enter email address:  ')
phone_number = input ('Enter the phone number:  ')
# Format the phone number
formatted_phone_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
job_title = input ('Enter the Job Title:  ').title()
id_number = input ('Enter the Id Number:  ')
format_id = f"{id_number[:2]}-{id_number[2:7]}"
color_hair = input ('Enter color hair:  ').capitalize()
color_eyes = input ('Enter color eyes:  ').capitalize()
start_month = input ('Enter Start Month:  ').capitalize()
status = input ('Are you in training?(Yes or No):  ')

# Accept only "Yes" or "No" for training status
while True:
    status = input('Are you in training? (Yes/No): ').capitalize()
    if status == 'Yes' or status == 'No' or status == 'Y' or status == 'N':
        break
    else:
        print(f'Invalid input. Please enter either "Yes" or "No".')
        
#print Id Card
print ('The Id Card is: ')
print ('-' *40)
# Align the last and first names
print (f'{last_name.ljust(15)}, {first_name.ljust(15)}')
#Align Email
print (f'{job_title.ljust(30)}')
# Align id number
print (f'{format_id.ljust(30)}\n')
# Align email
print (f'{email.ljust(30)}')
# Align Phone number
print (f'{formatted_phone_number.ljust(30)}\n')
# Align Color Hair and Eyes
print (f'Hair:{color_hair.ljust(15)} Eyes:{color_eyes.ljust(15)}')
# Align Month and Status
print (f'Month: {start_month.ljust(13)} Training: {status.ljust(20)}') 
print('-' *40)
