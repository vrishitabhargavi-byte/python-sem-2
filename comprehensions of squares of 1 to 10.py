a=[1,2,3,4,5,6,7,8,9,10]
l=[i*i for i in a]
s={i*i for i in a}
d={i:i*i for i in a}
g=(i*i for i in a)
print(l)
print(s)
print(d)
for i in g:
  print(i)