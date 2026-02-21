
#single inheritance
#parent----> child class --proporties from parent class are acquired to child classs
#create the object
#parent class
class Employee:
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid
    def empdetails(self):
        print(self.name,self.empid)
    #

    #child class
class Manager(Employee):

    def approve_leave(self):
        print("Leave approved")

m=Manager("JOHN",7878)
m.empdetails()#from parent class
m.approve_leave()