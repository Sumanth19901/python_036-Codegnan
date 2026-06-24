n=int(input())
i=0
while i<=10:
    i+=1
    print(f"{n}*{i}={n*i}")


# # x=["a","b","c","d","e","f"]
# # i=len(x)-1
# # while i>=0:
# #     print(x[i])
# #     i-=1
# 
# 
# # x=["a","b","c","d","e","f"]
# # i=0
# # l=[]
# # while i<len(x):
# #     if i%2==0:
# #         l.append(x[i])
# #     i+=1
# # print(l)
# 
# 
# #{0:"a",1:"b",2:"c",3:"d",4:"e",5:"f"}
# # x=["a","b","c","d","e","f"]
# # y={}
# # i=1
# # while i<len(x):
# #     y[i]=x[i]
# #     i+=1
# # print(y)
# 
# 
# # x=["a","b","c","d","e","f"]
# # y={}
# # i=0
# # while i<len(x):
# #     y[x[i]]=i
# #     i+=1
# # print(y)
# 
# x=["a","b","c","d","e","f"]
# y={}
# i=0
# a=[]
# b=[]
# while i<len(x):
#     i+=1
#     if i%2!=0:
#         y[x[i]]=i    
# print(y)
# for k,v in y.items():
#     a.append(k)
#     b.append(v)
# print(a)
# print(b)
# di={}
# for i in  range(len(b)):
#     di[b[i]]=a[i]
# print(di)
#  
