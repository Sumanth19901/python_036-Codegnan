# def rec(n):
#     if n==10:
#         return
#     else:
#         print(n)
#         rec(n-1)
#     
# rec(0)

# def rec(n):
#     if n==-1:
#         return
#     else:
#         print(n)
#         rec(n-1)
#         
# rec(10)

def Rec_fact(n):
    if n==1:
        return 1
    else:
        return n*Rec_fact(n-1)
print(Rec_fact(5))