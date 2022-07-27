# iterating tuples

myTuple = (1, 2, 3)

for tup in myTuple:
    print(tup)

print('myList1 = [(1, 2, 3), (4, 5, 9), (6, 7, 8)]')
myList1 = [(1, 2, 3), (4, 5, 9), (6, 7, 8)]
print(len(myList1))

for l in myList1:
    print(l)

# tuple unpacking, only works if all the tuples in the list are of same size
# otherwise gives error in iteration

for (a, b, c) in myList1:
    print(a)
    print(c)
