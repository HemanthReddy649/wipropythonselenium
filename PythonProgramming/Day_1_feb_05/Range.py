#all numbers should be integers
# step size cannot be zero

#range does
#fetch values at the index

#usage
#fast iteration
#loops and indexing


# fetch the values at the index
a = range(5)
print(a[1])
print(a[3])

a1 = range(2, 5)
print(a1[1])

# for loop
a = range(2, 5)
for i in a:
    print(i)

a = range(2, 5, 3)
for i in a:
    print(i)

a = range(2, -15, -3)
for i in a:
    print(i)

# rule: all numbers should be integers
# senario
for attempt in range(3):
    pin = input("Enter the pin: ")
    if pin == "1234":
        print("Access granted")
        break
    else:
        print("Try Again")

# sinario: Apply discount based on the position(index)
prices = [100, 200, 300, 400]
for i in range(len(prices)):
    if i % 2 == 0:
        print("Discount applied on item {1}")

# senario
import time

for second in range(10):
    print("Checking the status at {second} sec")
    time.sleep(1)
"""

"""  # check whether a number falls within a given range 1st


def check_range(num, start, end):
    if start <= num <= end:
        return "Number is within the range"
    else:
        return "Number is outside the range"


print(check_range(10, 5, 15))


# even numbers 2nd
def print_even():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)


print_even()


# sum numbers 3rd
def sum_numbers():
    total = 0
    for i in range(1, 101):
        total += i
    return total


print(sum_numbers())

# divisible by 5 4th
for i in range(1, 101):
    if i % 5 == 0:
        print(i)

# list of numbers form 50 to 100 5th
numbers = list(range(50, 101, 5))
print(numbers)

# print square of each number 6th
for i in range(1, 11):
    print(i * i)

# print -10 to 10 7th
for i in range(-10, 11):
    print(i)