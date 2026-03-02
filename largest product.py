a=[-7,-1,3,4,6,9]
a.sort()
p1=a[-1]*a[-2]*a[-3]
p2=a[0]*a[1]*a[-1]
print("largest product is:",max(p1,p2))