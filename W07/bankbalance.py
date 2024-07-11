current_checking_balance = float (input("What's your current checking balance? "))
current_savings_balance = float(input("Whats your current savings balance? "))
save_account = float(input("How much do you want transfer to the savings account? "))

if current_checking_balance <= save_account:
    print("You can't save more than you have in your checking account")
    print(f"Because you have a total of ${current_checking_balance} in your checking account")
elif:
    proceed_input = input("Do you want to proceed with the transaction? Y or N: ").strip().upper()
    proceed = proceed_input == "Y"

        if proceed:
            print("Your transaction will be processed")
        else:
            print("Your transaction has been canceled")
else:
    total_checking = current_checking_balance - save_account
    total_savings = current_savings_balance + save_account
    print(f"You have transferred ${save_account}")
    print(f"You have now ${total_savings} in the savings account")
    print(f"You have a total of ${total_checking} in the checking account")
