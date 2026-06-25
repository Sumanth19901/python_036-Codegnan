print((lambda :"this is the new way of function")())
result=(lambda:"this is the new way of function")
print(result())

print((lambda x:x*x)(10))

result=lambda x:x*x
print(result(10))

print((lambda x,y,z:x  if  x>y and  x>z else y if  y>z and y>x else z)(10,20,30))

l=[1,2,3,4,5,6]
print((lambda l:(i for i in l if  i%2==0)