# Cash Point (ATM) Program
# Author: Samuel Etong Inyang 

from pathlib import Path 

BALANCE_FILE = Path(__file__).parent / "balance.txt"
PIN = 1234



def write_balance(amount):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(amount))


def read_balance():
    try:
        with open(BALANCE_FILE, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        write_balance(5000)  
        return 5000


def mobile_top_up():
    balance = read_balance()
    print("Welcome to Mobile Top-Up.")
    try:
        top_up_amount = int(input("How much would you like to top up (£): "))
        if top_up_amount <= 0 or top_up_amount > balance:
            print("Invalid top-up amount or insufficent funds .")
            return
        balance -= top_up_amount
        write_balance(balance)
        print(f"\nTop-up successful. £{top_up_amount} debited.")
        print(f"New balance: £{balance}")
    except ValueError:
        print("Invalid input. Please enter a number.")


def cash_withdrawal():
    balance = read_balance()
    print("Welcome to Cash Withdrawal.")
    try:
        cash_amount = int(input("Enter amount to withdraw (£): "))
        if cash_amount <= 0 or cash_amount > balance:
            print("Insufficent amount.")
            return
        balance -= cash_amount
        write_balance(balance)
        print(f"£{cash_amount} withdrawn. New balance: £{balance}")
    except ValueError:
        print("Invalid input. Please enter a number.")


def balance_check():
    balance = read_balance()
    input("You have chosen Balance Check.\nPress Enter to continue...")
    print(f"Your current account balance is: £{balance}")


def order_statement():
    print("Order Statement:")
    print("1) Email")
    print("2) Post")
    try:
        choice = int(input("Please choose (1 or 2): "))
        if choice == 1:
            print("Your statement has been sent via email.")
        elif choice == 2:
            print("Your statement will be sent by post.")
        else:
            print("Invalid option.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")


def change_pin():
    global PIN
    print("You have chosen to change your PIN.")
    proceed = input("Would you like to proceed? (Y/N): ").strip().upper()
    if proceed == "Y":
        try:
            old_pin = int(input("Enter your current PIN: "))
            if old_pin == PIN:
                new_pin = int(input("Enter your new 4-digit PIN: "))
                if 1000 <= new_pin <= 9999:
                    PIN = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PIN must be a 4-digit number.")
            else:
                print("Incorrect old PIN.")
        except ValueError:
            print("Invalid input. PIN must be numeric.")
    else:
        print("PIN change cancelled.")


def main_menu():
    print("\n Cash Point ATM ")
    print("1) Mobile Top-Up")
    print("2) Cash Withdrawal")
    print("3) Balance Check")
    print("4) Order Statement (Email or Post)")
    print("5) Change PIN")
    print("6) Quit ")

    try:
        option = int(input("Please choose an option (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number from 1-6.")
        return
    if option == 1:
        mobile_top_up()
    elif option == 2:
        cash_withdrawal()
    elif option == 3:
        balance_check()
    elif option == 4:
        order_statement()
    elif option == 5:
        change_pin()
    elif option == 6:
        exit()
    else:
        print("Invalid selection. Please choose between 1 and 6.")

while True:
    main_menu()
