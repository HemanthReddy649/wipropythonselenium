class A:
    def show(self):
        print("Class A")
class B(A):
    pass
   # def show(self):
    #    print("Class B")
class C(A):
    pass
    #def show(self):
     #   print("Class C")
class D(B,C):
    pass
    #def show(self):
     #   print("Class D")

d=D()
d.show()
print(D.mro)

#method from left to right

#D,B,C,A