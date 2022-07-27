# Use for, .split(), and if to create a Statement that will print out words that start with 's':
#
# st = 'Print only the words that start with s in this sentence'

st = 'Print only the words that start with s in this sentence'
listWords = st.split()
print(listWords)

for word in listWords:
    if word.startswith('s'):
        print(word)

# Use range() to print all the even numbers from 0 to 10.

listNumbers = []

listNumbers = [n for n in range(0, 51) if n % 3 == 0]

print(listNumbers)

# Go through the string below and if the length of a word is even print "even!"
#
# st = 'Print every word in this sentence that has an even number of letters'

str = 'Print every word in this sentence that has an even number of letters'

listWords1 = str.split()

for word in listWords1:
    if len(word) % 2 == 0:
        print(word)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

listNumbers1 = range(1, 100)

for num in listNumbers1:
    print(num)
    if (num % 3 == 0) and (num % 5 == 0):
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print(num)
        print('Fizz')


def myfunc(string1):
    length = len(string1)
    print(len(string1))
    count = 0
    dummyString = ''

    while count< len(string1):
        if(count % 2 ==0):
            dummyString = dummyString + string1[count].upper()
        else:
            dummyString = dummyString + string1[count].lower()
        count += 1

    return dummyString


print(myfunc('abc'))