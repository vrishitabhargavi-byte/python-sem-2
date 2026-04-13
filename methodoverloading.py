class Overloading:
  def add(self,a,b,c=0):
    return a+b+c
s=Overloading()
print(s.add(10,20))
print(s.add(10,20,30))