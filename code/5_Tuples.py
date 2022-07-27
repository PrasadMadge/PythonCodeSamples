# tuples are immutable, they cannont be changed, you cannot grab and change
# intstead of using [] we use ()
# when to use tuple instead of list, when we want to make sure that the data should not change, data integrity


t = (1, 2, 3, 'string', 1, 1)

myList = [1, 2, 3]

print(type(t))
print(type(myList))

# grabbing as per indexing
print(t[3])

# counting a specific element in tuple
print(t.count(1))

# index of an element, not the value
print(t.index(2))

# checing immutubility
# t[0] = 'New' gives error
