bank_accounts = []
account_balances = []
account_name = ''
account_balance = 0
sum = 0
average = 0
highest = 0
highest_name = ''


while account_name != "quit":
    print("Enter the names and balances of bank accounts (type: quit when done)")
    account_name = input("What is the name of this account?: ")
    if account_name != "quit":
        bank_accounts.append(account_name)
        account_balance = float(input("What is the balance? "))
        account_balances.append(account_balance)
    
print()
print("Account Information: ")
for i in enumerate(bank_accounts):
    print(f"{i}. {bank_accounts[i]} --${account_balances[i]}")
    if account_balances[i] > highest:
        highest = account_balances[i]
        highest_name = bank_accounts[i]

for i in account_balances:
    sum +=1
    
print(f"\nThe total balance is: {sum}")
print(f"The average is {average}")
print(f"The highest = {highest}")

edit = input("Do you want to update an account?")
if edit.lower() == 'yes':
    while edit.lower() != 'no':
        index = int(input("What account index do you want to update? "))
        new_item = float(input("What is the new amount? "))
        account_balance[index] = new_item
        edit = input("Do you want to update an account?")
  
    
