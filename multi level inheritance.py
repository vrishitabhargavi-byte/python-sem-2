class A:
  def display_A(self):
    print("I am from class A")
class B(A):
  def display_B(self):
    print("I am from class B")
class C(B):
  def display_C(self):
    print("I am from class C")
s=C()
s.display_A()
s.display_B()
s.display_C()