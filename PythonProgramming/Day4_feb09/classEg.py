# class is a bule print or a template
#which describes the sate/ behaviour of its object
from symtable import Class
#data is put in variables
#behaviour put in funtion
class Student:
    #data or the properties
    studentname="Ravi"
    studentId=677877

    # self is used to access the  attributes of the class we defined
    #it is automatically loaded
    #self represents the instance of the class

#crreate a fuction to access the data
    def displaystudentDetails(self):
        print(self.studentname)
        print(self.studentId)

#create the object
a=Student()
a.displaystudentDetails()

