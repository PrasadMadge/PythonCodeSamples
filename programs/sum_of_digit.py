# Python program to display all integers within the range 100-200
# whose sum of digits is an even number
# https://pythonistaplanet.com/python-programming-exercises-and-solutions/

def sum_of_digit():
    numbers = range(100, 201)

    for n in numbers:
        sum = 0
        temp = n
        while n > 0:
            sum = sum + (n % 10)
            n = int (n / 10)
        
        if sum % 2 == 0:
            print(f"sum is {sum}")
            print(temp)


sum_of_digit()
