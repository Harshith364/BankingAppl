chance = 3
x = 0
while chance != 0:
    pin = int(input("Enter your pin: "))
    if pin == 4321:

        while True:
            if chance == 0:
                break
            n = int(
                input("\n Enter 1 for deposit \n Enter 2 to withdraw \n Enter 3 to check account balance \n Enter 4 to exit \n "))
            if n == 1:
                amnt = int(input("Enter amount to deposit: "))
                if x == 0:
                    x = amnt
                    print("AMOUNT DEPOSITED")
                else:
                    x += amnt
                    print("AMOUNT DEPOSITED")
            if n == 2:
                amnt = int(input("Enter amount to withdraw: "))
                if amnt == 0:
                    print("Enter sufficient amount to withdraw")
                elif amnt > x:
                    print("In Sufficient balance!!")
                else:
                    x = x-amnt
                    print(amnt, "rs = WITHDRAWN\n", x, "rs = REMAINING")
            if n == 3:
                print("BANK BALANCE = ", x, "rs")

            if n == 4:
                print("  PLEASE TAKE THE RECEIPT \n     THANK YOU!")
                break

    else:
        print("Please enter a valid pin!")
        chance -= 1
        if chance == 0:
            print("Try again and please enter a valid pin")
