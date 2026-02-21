#poly morpism means taking many forms
#same method?function name will be send acros the different method will behave differently depending on the
#object type
# #input arguments
#class implementation

print(len("python")) #string
print(len([1,2,3])) #list
print(len({1,2,3}) )#list

#input arguments no of arguments/datatypes

class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
c=calculator()
print(c.add(5))
print(c.add(5,10.5))
print(c.add(5,15))

#runtime polymorphism is supported
#achieved method overriding - child class method will override the parent class method

class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
a=Dog()
a.sound()


