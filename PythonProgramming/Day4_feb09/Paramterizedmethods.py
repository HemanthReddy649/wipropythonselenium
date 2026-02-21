#it allows the same method tp behave differently for diff inputs

#parameterized methods (multiple parameters)

class Calculator:
    def add(self,a,b):
        print(a+b)
c=Calculator()
c.add(10,50)
c.add(5,7)

#default parameters
class Test:
    def run(self, browser="chrome"):
        print("Running on",browser)
t=Test()
t.run()
t.run("Fire fox")


#*args parametizedd methods
