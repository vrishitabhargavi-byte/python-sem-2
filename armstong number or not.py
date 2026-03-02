n=int(input())
d=len(str(n))
sum=0
temp=n
while n!=0:
  rem=n%10
  sum=sum+(rem**d)
  n=n//10
if temp==sum:
  print("Armstrong Number")
else:
  print("Not Armstrong Number")