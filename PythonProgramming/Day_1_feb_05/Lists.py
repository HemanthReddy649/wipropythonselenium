empty_list=[]
numbers=[1,2,3,4,8,3,7,5]
mixeddata=[1,"hello",True,6.67,1]
nested=[[1,2],[3,4]]

#accessing the list elements (indexing concept)

print(mixeddata[1])
print(mixeddata[2])

#modifying data

mixeddata[4]=6
print(mixeddata)

#ADD ELEMENTS #insert at index

mixeddata.insert(5,10)
print(mixeddata)

#append will add at end
mixeddata.append("john")
print(mixeddata)

#remove elements

mixeddata.remove("hello")
print(mixeddata)

#push,pop

mixeddata.pop()
print(mixeddata)

mixeddata.pop(1)
print(mixeddata)

#index list methods

numbers.sort()
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


print(numbers.count(3))


print(numbers.index(3))


fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)
for i,a in enumerate(fruits):
    print(i,a)


#slicing

s=["a","b","c","r","f"]

print(s)


#slicingg

print(s[2:5])

#ommit sart and end index
a=len(s)
print(s[1:a-1])


#extends

numbers=[1,3,5]
even_numbers=[2,4,6]

numbers.extend(even_numbers)
print(numbers)

#list comprehensions

