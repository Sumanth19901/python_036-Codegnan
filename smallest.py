a,b,c=map(int,input().split())
#smallest number
smallest=a
if b<smallest:
    smallest=b
if c<smallest:
    smallest=c
print(smallest)
#gratest number
gratest=a
if b>gratest:
    gratest=b
if c>gratest:
    gratest=c
print(gratest)