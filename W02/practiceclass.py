#[3:56 PM] Pires, Sergio Ricardo
#Python functions
# lower()
# print(f'Your name is {name.lower()} and your age is {age}')
 
# upper()
# print(f'Your name is {name.upper()} and your age is {age}')
 
# capitalize()
# print(f'Your name is {name.capitalize()} and your age is {age}')
 
# title()
# print(f'Your name is {name.title()}')
 
# swapcase()
# print(f'Your name is {name.swapcase()}')
 
# length()
# print(f'Your name has {len(name)} characters.')
 
# Removing Whitespace (left)
# new_string = "  Hello, World!  "
# print("Stripped String (left):", new_string.lstrip())
 
# Removing Whitespace (right)
# print("Stripped String (right):", new_string.rstrip())
 
# Removing Whitespace (both sides)
# print("Stripped String (both sides):", new_string.strip())
 
# Replacing Substrings
# print("Replace 'Hello' with 'Hi':", new_string.replace("Hello", "Hi"))
 
# count('a')
# print(f'There are {name.count('a')} "a\'s" on {name}')
 
# new line
# print(f'Your name is {name} \nYour age is {age}')
 
# print (with format parameter)
# print(f'Your name is {name:20} and your age is {age}')

full_name = "  JOSHUA STONE  "
email = "josh.Stone#gmail.com"
address = "101 E Viking St, Rexburg, ID 83460"
city = "rexburg???"
state = "ID"
zip = "83460-"
phone = "208-496-1411"

print(f"{full_name.title().strip()}")
print(f"{email.lower().replace("#","@")}")
print(f"{address.replace(", Rexburg, ID 83460","")}")
print(f"{city.title().replace("???","")}")
print(f"{state.title()}")
print(f"{zip.replace("-","")}")
print(f"({phone[:3]}){phone[3:7]}-{phone[8  :]}")
