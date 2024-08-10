import time  

print("Please insert Your CARD")
time.sleep(5)

password=1234

pin=int(input("enter your pin"))

balance=5000

if pin==password:
    while True:
        print("""
            1== balance
            2== withdraw balance
            3== deposit balace
            4== exit
            """
            )
        
        try:
            option=int(input("please eneter your choise"))
        except:
            print("please enter valid option")

        if option == 1:
            print(f"your current balance is {balance}")

        if option == 2:
            withraw_amount=int(input("please enter withraw_amount"))
            balance=balance=withraw_amount

            print(f"{withraw_amount}is debited from your account")
            print(f"your current balance is {balance}")

        if option==3:
            deposit_amount=int(input("please enter deposit_amount"))
            balance=balance+deposit_amount
            print(f"{deposit_amount}is credited to your account")
            print(f"your update balance is {balance}")

        if option==4:
            break
        
        
    else:
        print("wrong pin Please try again")