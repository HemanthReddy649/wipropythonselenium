# lamda functions - anonymous (nameless) functions,one line,for simple operations

# syntax
# lambda arguments :expression

# rules : it can have any number of arguments
# must have only one expression
# the expression is automatically returned

# function -function name,arguments, return type,code,

#normal function

def add(a,b):
    return a+b
print(add(5,3))

#lamda fuction

add = lambda a,b: a+b
print(add(5,3))


#square of num

square=lambda a:a*a
print(square(5))

#even or odd

result=lambda a:"even" if a%2==0 else "odd"
print(result(5))

max=lambda a,b: a if a>b else b
print(max(4,5))


#in built functions in lambda

# filter , map and reduce in built functions in lambda

#FILTER -select data - filtering the data

# map - transform the data

#reduce -aggregate the data


numbers=[1,2,3,4,5,6]
evens = list(filter(lambda x: x%2==0,numbers))
print(evens)

#filter the failed testcases

status =['Pass','fail','pass','fail']
failed=list(filter(lambda x:x=="fail",status))
print(failed)

#filter + ve numbers
nums = [-5, 10, -3, 7, 0, 2]
positive=list(filter(lambda x:x>=0,nums))
print(positive)

#Filter non-empty strings

data = ["hello", "", "world", "", "python"]
non=list(filter(lambda x:x!="",data))
print(non)

#reduce-aggregate - combining to a one single result

from functools import reduce
nums=[10,20,30,40]
print(reduce(lambda x,y:x+y,nums))
nums=[10,20,30,40]
print(reduce(lambda x,y:x-y,nums))


#multiply,maximum, minimum value

nums=[10,20,30,40]
print(reduce(lambda x,y:x*y,nums))

nums=[10,20,30,40]
print(reduce(lambda x,y:x if x>y else y,nums))

nums=[10,20,30,40]
print(reduce(lambda x,y:x if x<y else y,nums))

#map-transform the data- the function is applied to every element


nums=[10,20,30,40]
squares=list(map(lambda x:x*x,nums))
print(squares)

#sorting the data

data=[(10,90),(20,350), (50,40)]
sorteddata=sorted(data,key=lambda x:x[1])
print(sorteddata)

marks={"A":75,"B":90,"C":60}
sorted_marks=dict(sorted(marks.items(),key=lambda x:x[1]))
print(sorted_marks)