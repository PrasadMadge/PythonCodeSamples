# map and filter before lambda express


# needs for loop for output
# syntax map(functionName, listName)

def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

print(map(square, my_nums))  # <map object at 0x108cd9ea0>


for item in map(square, my_nums):
    print(item)

#  to get in list
print(list(map(square, my_nums)))  # [1, 4, 9, 16, 25]


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]


names = ['Prasad', 'Cools', 'Andy']

print(list(map(splicer, names)))

numbers1 = [1, 2, 3, 4, 5, 6]


def checkEven(num):
    if num % 2 == 0:
        return True


print(filter(checkEven, numbers1))
# <filter object at 0x1069f7ee0>

for n in filter(checkEven, numbers1):
    print(n)

print(list(filter(checkEven, numbers1)))
# [2, 4, 6]

#  now lambda expression, it is a breakdown of a method in the end.
# lambda expression is also an anonuymous expression.
# only used when you dont want to intialise the method and use it one time
# since we dont use it is is used in conjuction with map and filter method.

#  basic syntax
square = lambda num: num ** 2

print(square(5))
# 25

# with map

print(list(map(lambda num: num ** 2, numbers1)))

#  [1, 4, 9, 16, 25, 36]
# with filter

print(list(filter(lambda num: num % 2 == 0, numbers1)))

# [2, 4, 6]