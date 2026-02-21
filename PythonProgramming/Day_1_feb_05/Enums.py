fruits=["orange","cherry","kiwi"]
for index,fruit in enumerate(fruits):
    print(index,fruit)

    #enumerate with start value changed
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)


 #enumerate with strings
word="Python"
for i,ch in enumerate(word):
    print(i,ch)

    # enumerate with tupless

fruits=("orange","cherry","kiwi")
for index,fruit in enumerate(fruits):
    print(index,fruit)

#real time senario

test_cases =["Login","Signup","Checkout"]
for i,a in enumerate(test_cases,1):
    print(f"Executing testcase {i}:{a}")

#accessing of enumerate values

a=["god","is","great"]
b=enumerate(a)
nxt_val=next(b)
print(nxt_val)
print(nxt_val)

characters = [
    "krillin","goku","gohan","piccolo",
    "krillin","goku","vegeta","gohan",
    "piccolo","piccolo","goku","vegeta",
    "goku","piccolo"
]

# create a dictionary with empty lists
character_map = {character: [] for character in set(characters)}

# use enumerate to store indexes
for index, character in enumerate(characters):
    character_map[character].append(index)

# print only duplicates
for character, indexes in character_map.items():
    if len(indexes) > 1:
        print(character, "->", indexes)
