class A:
    def display_A(self):
        print("I am from class A")
class B(A):  
    def display_B(self):
        print("I am from class B")
class C(A): 
    def display_C(self):
        print("I am from class C")
s1 = B()
s2 = C()
s1.display_A()
s1.display_B()
s2.display_A()
s2.display_C()