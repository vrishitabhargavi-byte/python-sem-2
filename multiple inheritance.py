class a:
    def display_a(self):
        print('i am from class a')
class b:
    def display_b(self):
        print('i am from class b')
class c(a,b):
    def display_c(self):
        print('i am from class c')
s=b()
s=c()
s.display_a()
s.display_b()
s.display_c()