import math
# Insert data
age = int(input("What\'s your age? "))

#calculus
f_age = age + 1


#print
print (f'Next year your age will be {f_age}\n')


eggs = int(input("How many eggs cartoon do you have? "))
c_eggs = eggs * 12
print (f'You have {c_eggs} eggs\n')

cookies = int(input("How many cookies do you have? "))
q_people = int(input("How many people are in the class? "))

quantity_per_person = float(cookies / q_people)
print(f'Each student may have {quantity_per_person:.2} cookies')