print("is the student is present ")
collage=input()
if collage=="yes":
    print(" in the collage")
    block=input()
    if block=="yes":
        print("in the block")
        floor=input()
        if floor=="yes":
            print("in the floor")
            room=input()
            if room=="yes":
                print("in the class")
            else:
                print("in the floor")
        else:
            print("in the block")
    else:
        print("in the collage")
else:
    print("adsent")