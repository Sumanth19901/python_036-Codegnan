def  check_balance():
    global Balance
    print(f"Your current balance is: {Balance}")

def  Deposite(money):
    global Balance
    Balance += money
    print(f"amount {money} succefully credited")
    print(f"Your current balance is: {Balance}")

def  account_details()


while: True:
    print("1. Check Balance")
    print("2. Deposite Money")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        check_balance()
    elif choice == '2':
        amount = float(input("Enter amount to deposite: "))
        Deposite(amount)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
    

    
