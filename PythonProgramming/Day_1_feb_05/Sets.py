#sets do not allow duplicate elements it only contains unique data
#unordered collection

#creeate  a set integer type
stu_id={112,113,114,115,115}
print(stu_id)

#creeate  a set dtr type
letters={'a','b','c','d','e'}
print(letters)

#mixed

mixed_set={"hello",1,-7,8,9}
print(mixed_set)

#empty

empty_set=set()
print(empty_set)


#add
s={1,2,3}
s.add(4)
print(s)

#update
s.update([6,7,8])
print(s)

#remove(
s.remove(2)
print(s)

#discard

s.discard(8)
print(s)

#pop
s.pop()
print(s)

#clear
s.clear()
print(s)

#set operations

#union

a={1,2,3}
b={3,4,5}
print(a.union(b))

#intersection

print(a.intersection(b))

#difference

print(a.difference(b))

#symmetric difference
print(a.symmetric_difference(b))

#issubset
a={1,2}
b={1,2,3}
print(a.issubset(b))
#issuperset
print(b.issuperset(a))

#disjoint


print(a.isdisjoint(b))