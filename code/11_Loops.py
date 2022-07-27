# for loops

names = ['A', 'B', 'C']

for name in names:
    print(name)

# name is alias name, use : in the end.
myLists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for l in myLists:
    print(l)

# print only even numbers in the list

for l in myLists:
    # check for even here
    if (l % 2 == 0):
        print(l)

myString = 'Hello world'

for character in myString:
    print(character)
