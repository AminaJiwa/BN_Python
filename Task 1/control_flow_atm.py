
class control_flow_atm:
    balance = 0
    pin = 1234
    userPin = int(input("Please enter your pin: "))

    if pin != userPin:
        print("Your pin value doesn't match.")
    else:
        print(balance)
        choice = input("Would you like to deposit/withdraw some money? Please enter y for yes and n for no.")

        while choice:
            if choice == "n":
                print("Thank you, have a nice day.")
                break
            elif choice == "y":
                amount = int(input("Please enter the amount using a - sign if it is a withdrawal. "))
                balance += amount
                print("Your updated balance: " + str(balance))
                break
            else:
                choice = input("Would you like to deposit/withdraw some money? Please enter y for yes and n for no.")
