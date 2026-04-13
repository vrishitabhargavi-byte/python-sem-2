class A:
  def display_A(self):
    print("I am from class A")
class B(A):
  def display_B(self):
    print("I am from class B")
s=B()
s.display_A()
s.display_B()