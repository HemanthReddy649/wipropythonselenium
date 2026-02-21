#function is a block of code that performs specific task
#def function name()

#defaultfuntion with no parameters

def printdata():
    print("Hello world")

#call the function
printdata()

#functiion with parameters

def printdata(name):
    print("Hello ",name)

#pass the argument
printdata("Tina")
printdata("Rita")

#return statment
#to return the function value return statment is used

def square_root(num):
    result=num*num
    return result

#function call
a=square_root(5)
print('square:',a)

#function pass
def func_pass():
    pass
#call the function
func_pass()

#multipel return valuens

def cal(a,b):
    return a-b,a+b,a*b
add,sub,mul=cal(10,5)
print(add)
print(sub)
print(mul)

#function calling a another function

def areaofrect(len,width):
    return len*width

def areaofsq(side):
    return side*side
value=areaofrect(4,6)

a=areaofsq(value)
print(a)

#funtion with loop

def even(limit):
    for i in range(2,limit+1,2):
        print(i)
even(10)


#function with if else condition
def even(limit):
    if limit%2==0:
        return "even"
    else:
        return "odd"
print(even(1))
print(even(2))

