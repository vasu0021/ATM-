import time  

print("Please insert Your CARD")
time.sleep(5)

password=1234

pin=int(input("enter your pin "))

balance=5000
transaction_history=[]

if pin==password:
    while True:
        print("""
            1== balance
            2== withdraw balance
            3== deposit balace
            4== PIN change
            5== View Transaction history
            6== exit
            """
            )
        
        try:
            option=int(input("please eneter your choise "))
        except:
            print("please enter valid option")

        if option == 1:
            print(f"your current balance is {balance}")

        if option == 2:
            withraw_amount=int(input("please enter withdraw_amount "))
            if withraw_amount<=balance:
                balance=balance-withraw_amount
                transaction_history.append(f"withdraw {withraw_amount}.new balance {balance}")
                print(f"{withraw_amount} is debited from your account")   
                print(f"your update balance is {balance}")        
            
            else:
                print("insufficient balance")

        if option==3:
            deposit_amount=int(input("please enter deposit_amount "))
            balance=balance+deposit_amount
            transaction_history.append(f"deposited{deposit_amount}. new balance{balance}")
            print(f"{deposit_amount}is credited to your account")
            print(f"your update balance is {balance}")
        
        if option == 4:
            new_pin=int(input("enter the new pin "))
            pin==new_pin
            print("pin is successfully changed")
            
            

        if option == 5:
            if transaction_history:
                print("transaction history")
                for transaction in transaction_history:
                    print(transaction)

            else:
                print("transaction history is not found")

        if option == 6:
            break
        
        
    else:
        print("wrong pin Please try again")