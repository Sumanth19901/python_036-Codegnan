vehicle=["bike","auto","car"]
user=input("choose the vehicle:")
if user in vehicle[0]:
    print("select the distance:")
    km=int(input())
    value=km*5
    if km<=8:
         print(value,'Rs/km')
    elif km>=9 and km<=15:
        print((km-10)*6+40)
    elif km>=16 and km<=25:
        print((km-8)*6+82)
    elif km>=26 and km<=30:
         print((km-8)*6+182)
    else:
        print("no rider")
if user in vehicle[1]:
    print("select the distance:")
    km=int(input())
    value=km*8
    if km<=10:
         print(value,'Rs/km')
    elif km>=11 and km<=19:
        print((km-8)*6+52)
    elif km>=20 and km<=29:
        print((km-8)*6+148)
    elif km>=30 and km<=60:
         print((km-8)*6+310)
    else:
        print("no rider")
if user in vehicle[2]:
    print("select the distance:")
    km=int(input())
    value=km*12
    if km<=50:
         print(value,'Rs/km')
    elif km>=51 and km<=80:
        print((km-8)*6+52)
    elif km>=81 and km<=120:
        print("toll amount")
        toll=int(input())
        print((km-8)*6+148+toll)
    elif km>=30 and km<=60:
         print((km-8)*6+310)
    else:
        print("no rider")  