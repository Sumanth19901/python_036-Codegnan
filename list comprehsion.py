# def values(n,l=[]):
#     for i in range(1,n+1):
#         if i%2==0:
#             l.append(i)
#         else:
#              l.append("odd")
#     return l
# 
# n=100
# print(values(n))


# n=100
# print([i for i in range(1,n+1) if i%2==0])

# 
# n=100
# print([i if i%2==0 else "odd" for i in range(1,n+1)])


# def values(n,l=[]):
#     for i in range(1,n+1):
#         if i%2==0:
#             l.append(i)
#         elif i%3==0:
#              l.append("odd")
#         elif i%5==0:
#             l.append("somthing")
#     return l
# 
# n=100
# print(values(n))


# n=100
# print([i if i%2==0 else "something" if i%2!=0 and i%5==0 else "odd" for i in range(1,n+1)])

l =[[i,j ] for i in range (5)  for j in range(5) ]
print(l)
        
