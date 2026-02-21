#descriptor - control the access of the object attributes

#_get_()
#_set_()
#_delete()

class Descr:
    def __get__(self,instance,owner):
        print("getting the value")
        return 10
class  Test:
    x =Descr();

t=Test();
print(t.x)


#this non-data descriptor -used only in __get__ descriptor
#data decriptor uses both get and set method

##__set__

class Mydesc:
    def __get__(self,instance,owner):
        return instance._value
    def __set__(self,instance,value):
        print("Setting the value")
        instance._value=value

class Test:
    x=Mydesc()
t=Test()
t.x=100
print(t.x)

#delete
class Name:
    def __get__(self,instance,owner):
        return instance._value
    def __set__(self,instance,value):
        print("Setting the value")
        instance._value=value
    def __delete__(self, instance):
        print("Deleting name")
class Person:
    name=Name()

p=Person()
p.name ="Harsha"
del p.name