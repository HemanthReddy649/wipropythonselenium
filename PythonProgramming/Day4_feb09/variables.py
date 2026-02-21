#variables = used to store the data
#instance variables - global variables at class level
#local variables - inside the method only
from tkinter.font import names


class Student:
    #class variables
    school ="st joseph convent"
    def __init__(self,name,marks):
        self.name=names#instance variable or global variable
        self.marks = marks#instance or global variable
    def show(self):
        schoolcity="Bangaloe"#local varaiable - scope in inside the methos
        print(self.marks,self.name)
        print(schoolcity)
        print(self.school)
s1=Student("harsha",85)
s2=Student("amit",90)
s1.show()
s2.show()