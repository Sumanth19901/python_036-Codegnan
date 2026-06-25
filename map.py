# #map
# def str(s):
#     x=""
#     for i in s:
#         x=i.upper()+x
#     return x
# 
# print(str("mapping"))
# print(list(map(str,"mapping")))


# def Len(l):
#     x=[]
#     for i in l:
#         x.append(len(i))
#     return x
# 
# l=["tcs","wipro","capgimini","zoho"]
# print(Len(l))
# print(list(map(lambda )))


def Cap(l):
    x=[]
    for i in l:
       x.append(i[0].upper()+i[1:])
    return x

l=["tcs","wipro","capgimini","zoho"]
print(Cap(l))
print(tuple(map((lambda x:x.capitalize()),l)))
result=filter((lambda x:x.startswith("t")),l)
print(list(result))

from functools import reduce