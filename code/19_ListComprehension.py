# list comp is a unique of quickly creating list in py
# no computational benefit but decreases code readibitily and make it in one liner.
# we can also add if condition and also else in the end of it.
#  in if statement the condition comes in the end.
#  in if else the condition comes in the beginning
#  also nested loops in list comp


name = 'Prasad'
myList = []

for n in name:
    myList.append(n)

print(myList)

# so now we can replace the whole above code with one liner
# copy the for loop line and remove the bottom one and n or alias name before it

myList1 = [n for n in name]
print(myList1)

#  creating a list of numbers using range

myList2 = [x ** 2 for x in range(0, 10)]
print(myList2)

#  what if you need to grab only the even numbers here

myList3 = [num for num in range(0, 11) if num % 2 == 0]
print(myList3)

#  List of temps in celcius
celcius = [0, 1, 2, 3, 4]

fahreneit = [(cel * (9 / 5.0) + 32) for cel in celcius]
print(fahreneit)

# list comp with if else
# create a list of even and odd

myListNum = [n if (n % 2 == 0) else 'ODD' for n in range(0, 11)]
print(myListNum)

# [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]


#  nested for loops in list comp

#  first the normal way without list comp

myNumbersList = []

for x in (1, 2, 3):
    for y in (100, 200, 300):
        myNumbersList.append(x * y)

print(myNumbersList)

#  now using list compo

myNumbersList1 = [x * y for x in (1, 2, 3) for y in (100, 200, 300)]
print(myNumbersList1)