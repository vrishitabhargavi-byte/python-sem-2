def sum(a,b):
    return a+b
n=int(input('enter number of additions'))
for i in range(n):
    a,b=map(int,input().split())
    result=sum(a,b)
    print(result)