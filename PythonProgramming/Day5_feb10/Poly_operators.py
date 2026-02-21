#operator polymorphism means
#the same operator behaves differently for diff data types or the objects
#+add numbers
#+joins the strings
#+merges the lists
#operator overloading in python
#pythin

#__add__()
#__sub__()
#__mul__()
#__eq__()
#__lt__
#__gt__

class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value+other.value
n1=Number(10)
n2=Number(20)
print(n1+n2)

#now + will work for the custom objects


class Numbersub:
    def __init__(self,value):
        self.value=value
    def __sub__(self,other):
        return self.value-other.value
n1=Numbersub(30)
n2=Numbersub(50)
print(n1-n2)

class Multiply:
    def __init__(self,value):
        self.value=value
    def __mul__(self, other):
        return self.value*other.value
n1=Multiply(50)
n2=Multiply(100)
print(n1*n2)


class Equal:
    def __init__(self,value):
        self.value=value
    def __eq__(self, other):
        return self.value==other.value
n1=Equal(50)
n2=Equal(50)
print(n1==n2)

class Greater:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

n1 = Greater(30)
n2 = Greater(20)

print(n1 > n2)

class Lower:
    def __init__(self, value):
        self.value=value
    def __lt__(self, other):
        return self.value < other.value
n1=Lower(10)
n2=Lower(20)
print(n1<n2)
