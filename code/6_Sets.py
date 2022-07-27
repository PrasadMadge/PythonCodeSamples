# unordered collection of unique elements
# cannont have single element more that 1 time

mySet = set()
print(mySet)
# returns an empty set

mySet.add(1)
print(mySet)

# prevents duplication, only unique
mySet.add(2)
mySet.add(2)
print(mySet)

# casting list to set
myList = [1,1,2,3]

print(myList)
print(set(myList))