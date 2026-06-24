# for i in range(4):
#     for j in range(4,0,-1):
#         print(j,end="")         
#     print()

# i=4
# j=4
# while i>=0:
#     print(i,j)
#     j
#     i-=1

# for i in range(4,0,-1):
#     for j in range(4,0,-1):
#         if i%2==0:
#             print(i,end="")         
#         print("")
# n=5
# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# n=5
# for i in range(1,6):
#     for j in range(n-i+1):
#         print("*",end="")
#     print()'

# n=5
# for i in range(1,6):
#     for j in range(n-i+1):
#         print("*",end="")
#     print()


n=5
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
n=5
for i in range(5):
    for j in range(5):
        if i==0  or j==n-3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    



n=5
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or j==n-1 or i==n-3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    
    
n=5
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()      
    
    

    