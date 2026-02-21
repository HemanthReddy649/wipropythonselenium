#dictionary items -key value
# similar to list and tuple
# for integers, tuples and strings -must be immutable
#list cannot be used in the key for the dict as it is mutable in nature

country={
    "india":"delhi",
    "canada" : "Ottawa",
    "England" : "london"
}

print(country)

#access the values with the keys

print(country["canada"])

#remove elements

del country["india"]
print(country)

#clear
#country.clear(
#print(country)

#iterate among the dictionary

for coun in country:
    print(coun)

#length of dict
print(len(country))

#for integer keys must be immutable

#integer as a key

my_dict={
    1:"one",
    2:"two",
    3:"three"
}
print(my_dict)

my_dict={
    1:"one",
    2:"two",
    3:"three",
    1:"four",
    4:"four"
}
print(my_dict)

#tuples as a key

my_dict ={
    (1,2):"one two",
    3:"three"
}
print(my_dict)

my_dict ={
    (1,2):"one two",
    3:"three",
    3:"four"
}
print(my_dict)

#list as a key XXXX

#my_dict={
 #   [1,2]:"one two",
  #  2:"hello"
#}
#print(my_dict)


#pop - removes the item with spec key



#update()-adds or changes the dict


#keys



#values()


#popitem() return the last inserted keyword



#copy returns the copy of dict



#dict inside the list

a=[
    {"id":"20402","name":"varun","role":"qA"},

    {"id":"20","name":"tharun","role":"q"},

    {"id":"202","name":"karun","role":"A"}
]
print(a[0])
print(a[0]["name"])

for emp in a:
    print(emp["name"],emp["role"])


a.append({"id":"202","name":"karun","role":"A"})
print(a)


a.pop(0)
print(a)



#search a item in the list

for emp in a:
    if emp["name"]=="karun":
        print(emp)
        break