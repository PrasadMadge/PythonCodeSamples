# Python program to check whether the given integer is a prime number or not
# a num divisible by only itself is a prime number
# for loop to check divisibility from 2 to number
# if divisible then check if number is number or not, if yes then prime

def prime_number(number):
    counter = 1
    while counter <= number:
        counter = counter + 1
        if number % counter == 0:
            if number == counter:
                print(number)
                print("Prime number")
                break
            else:
                print(number)
                print("No Prime number")
                break


prime_number(105)
