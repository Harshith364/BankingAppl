# ATM Machine COde


def deposit(amnt, bal):
    bal += amnt
    print("AMOUNT DEPOSITED")
    return bal


def withdraw(amnt, bal):
    if bal == 0:
        print("Enter sufficient amount to withdraw")
    elif amnt > bal:
        print("In Sufficient balance!!")
        return bal
    else:
        bal = bal-amnt
        print(amnt, "rs = WITHDRAWN\n", bal, "rs = REMAINING")
        return bal


def balance(bal):
    return bal


chance = 3
bal = 0
while chance != 0:
    pin = int(input("Enter your pin: "))
    if pin != 4321:
        print("Please enter a valid pin!")
        chance -= 1

        if chance == 0:
            print("Try again and please enter a valid pin")

    elif pin == 4321:

        while True:
            m = input(
                "\n Enter 1 for deposit \n Enter 2 to withdraw \n Enter 3 to check account balance \n Enter 4 to exit \n ")
            n = int(m)
            if n == 1:
                amnt = int(input("Enter amount to deposit: "))
                bal = deposit(amnt, bal)
            if n == 2:
                amnt = int(input("Enter amount to withdraw: "))
                bal = withdraw(amnt, bal)

            if n == 3:
                print("BANK BALANCE = ", balance(bal), "rs")

            if n == 4:
                print("  PLEASE TAKE THE RECEIPT \n     THANK YOU!")
                break
    if pin == 4321 and n == 4:
        break
