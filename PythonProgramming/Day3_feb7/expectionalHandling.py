#exceptions - rintime errors which will disrupt the norma; program filow
#benefits
#helps in debugging
#prevent from program crashing
#handle errors and expections in the code more effeciently

#try,except

#try -code to be executed
#expect -exception details cathing
#else :if the exception doesn't occur then else part will be excuted
#finally-mandated code
#custum exceptions
#mutliple exceptions are possible

try:
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide a number by 0")
except ValueError:
    print("please enter valid numbers")

#generic exception

try:
    a=5/0
except Exception as e:
    print(e)

#runs only no exceptuon occurs
else:
    print("Division successful")
finally:
    print("close the browser")


#custom exception - creating a own exception

age=int(input("Enter the age"))

if age<18:
    raise ValueError("Age must be 18 or above")

