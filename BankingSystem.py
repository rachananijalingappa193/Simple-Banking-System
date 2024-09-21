try:
    print(" WELCOME!!")
    choice = int(input("Enter your account type: \n 1) Current account\n 2) Saving account\n 3) Exit \n 4) Create new account\n"))
    account = ["123","456","789"]
    pinn = ["199","666","999"]
    balance = [200000.0,3900000.0,450000.34]
    def account_details(acc_num,pin):
        global account
        global pinn
        global balance
        amountt = int(input("1) Withdraw \n2) Deposite \n"))
        if amountt == 1:
            with_amount = float(input("Enter the withdrawl amount"))
            if with_amount < 0:
                print(f"enter the correct amount!!")
            else:
                if acc_num == account[0] and pin == pinn[0]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[0]}")

                    if with_amount <= balance[0]:
                        print("processing amount",with_amount)
                        return f"Your Remaining balance is: {balance[0] - with_amount}"
                    else:
                        return "Insufficient Balance"

                elif acc_num == account[1] and pin == pinn[1]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[1]}")
                    if with_amount <= balance[1]:
                        print("processing amount",with_amount)
                        return f"Your Remaining balance is: {balance[1] - with_amount}"
                    else:
                        return "Insufficient Balance"
                elif acc_num == account[2] and pin == pinn[2]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[2]}")
                    if with_amount <= balance[2]:
                        print("processing amount: ",with_amount)
                        return f"Your Remaining balance is: {balance[2] - with_amount}"
                    else:
                        return "Insufficient Balance"
                elif acc_num == account[3] and pin == pinn[3]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[2]}")
                    if with_amount <= balance[2]:
                        print("processing amount: ",with_amount)
                        return f"Your Remaining balance is: {balance[2] - with_amount}"
                    else:
                        return "Insufficient Balance"
                elif acc_num == account[4] and pin == pinn[4]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[2]}")
                    if with_amount <= balance[2]:
                        print("processing amount: ",with_amount)
                        return f"Your Remaining balance is: {balance[2] - with_amount}"
                    else:
                        return "Insufficient Balance"
                else:
                    return f"Please enter correct account number or pin"
        else:
            deposite = int(input("Please enter the amount to deposite: "))
            if deposite < 0:
                print("Enter the valid amount, amount cannot be negative")
            else:
                if acc_num == account[0] and pin == pinn[0]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[0]}")
                    return f"Your current balance is {balance[0]+deposite}"
                elif acc_num == account[1] and pin == pinn[1]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[1]}")
                    return f"Your current balance is {balance[1]+deposite}"
                elif acc_num == account[2] and pin == pinn[2]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[2]}")
                    return f"Your current balance is {balance[2]+deposite}"
                elif acc_num == account[3] and pin == pinn[3]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[3]}")
                    return f"Your current balance is {balance[3]+deposite}"
                elif acc_num == account[4] and pin == pinn[4]:
                    print(f"Yours account number is: {acc_num}")
                    print(f"Your account balance is: {balance[4]}")
                    return f"Your current balance is {balance[4]+deposite}"
    if choice == 3:
        print("You choosed to Exit")
    elif choice == 4:
            name = (input("Please enter your name: "))
            num = (input("Please choose your account number that should be 3 digit: "))
            if num == account[0] or num == account[1] or num == account[2]:
                print(f"the account number already taken please choose another number")
            else:
                newpin = int(input("Choose your pin: "))
                newbalance = float(input("Enter the ammount you want to deposit in your account"))
                account.append(num)
                pinn.append(newpin)
                balance.append(newbalance)
                print("Congradulation you have successfully created your account ")
    elif choice == 1 or choice == 2:
        acc_num = input("Please enter your account number: ")
        pin = input("Please enter your pin number: ")
        print(account_details(acc_num,pin))
    else:
        print("Please enter the Valid Choice")
except ValueError:
    print("Please enter correct value...")




