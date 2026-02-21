#constructors - first function of the class when an object of the class is created

#syntax __init__()
#we can parameterized the constructors
#self is mandatory

class Student:
    def __init__(self):
        print("Constructor is called")
s1=Student()

#parametrized constructors

#self.name is a instance variable (belong to object)
#if we dont assign it to the self.name the object will not remember the value
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
    def display(self):
        print(self.name,self.salary)
e1=Employee("harsha",50000)
e2=Employee("varun",6878)
e1.display()
e2.display()

#using * arguments in the constructor

#constructor overloading is supported by * args
#we can pass any number of parameter to the constructor using *args
class Numbers:
    def __init__(self,* args):
        self.values=args
n=Numbers(10,20,30)
print(n.values)
n=Numbers(10)
print(n.values)


#parent and child constructors

#super keyword for accessing parent constructor

class Parent:
    def __init__(self):
        print("I am the parent constructor")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child Constructor")

c=Child()
