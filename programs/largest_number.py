# Python program to find the largest number in a list without using built-in functions

def largest_number():
    list_of_numbers = range(1, 200)
    max_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number > max_number:
            max_number = number
    print(max_number)


largest_number()
