import random
num=[random.randint(1,100) for i in range(20)]
print(num)
print("Minimum Number:",min(num))
print("Maximum Number:",max(num))
print("Average Number:",sum(num)//len(num))
ec=0
for i in num:
  if i%2==0:
    ec=ec+1
print("Even Numbers count are:",ec)