# inbuilt key word function
# range, creats a list of integers
# enumerate, creates a tuple out of string mapping indexes
# string -> tuple

# zip, zips to different lists into a tuple
# 2 lists -> tuple



# range, creates a list as per need of numbers, start, end and diff

myList = [1, 2, 3]
# since it is a common task you can iterate through it, range keyword

# range(start , stop, step)
for num in range(3, 10, 2):
    print(num)

print(list(range(0, 10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2 enumerate
# applied to string, returns tuples intrestingly
indexCount = 0

for letter in 'abcde':
    print(f'At index {indexCount} the letter is {letter}')
    indexCount += 1

# we can use the inumerate operator to use the above

word = 'abcde'
indexCount = 0

for letter in word:
    print(word[indexCount])
    indexCount += 1

for letter in enumerate(word):
    print(letter)

# returns tuples  (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

for a, b in enumerate(word):
    print(a)
    print(b)
    print('\n')

#   0
# a
#
#
# 1
# b
#
#
# 2
# c
#
#
# 3
# d
#
#
# 4
# e

# ZIP, opposite of enumerate, zips together 2 lists

myList1 = [1, 2, 3, 4, 5]
myList2 = ['a', 'b', 'c']

for item in zip(myList1, myList2):
    print(item)

# (1, 'a')
# (2, 'b')
# (3, 'c')

# only zipped till 3, ignored 4, 5 as the other list was uneven without any error.

