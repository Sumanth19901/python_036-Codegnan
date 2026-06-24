print("welcome to ATM for account details and amount \n 'insert ATM' \n if inset plese click Yes/NO")
user=str(input())
yes={1:'Account_Details',2:'Amount_Deposite',3:''}
if yes in user:
    print(yes)
elif no in user:
    print("insert the ATM Card properly")