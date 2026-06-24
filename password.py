capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small="abcdefghijklmnopqrstuvwxyz"
num="0123456789"
symble="!@#$%^&*"

user=input("Enter Password:")
i=12
if i<=len(user):
    for i in user:
        if user in capital:
            capitel = True
        elif user in small:
            samll = True
        elif user in num:
            num = True
        elif user in symble:
            symble = True
else:
    print("re-enter password")