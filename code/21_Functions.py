# same like java, code reuse
# def keyword, allows to create func,
# specific syntax, proper indentation and struction
# def name_of_function():  // syntax
# # '''
# Docstring explains function
# '''
# snake casing, all lower caps, and _, python convention
#

def say_hello():
    print('Hello')


say_hello()


# prints hello above

# overwriting the method

def say_hello(name):
    print('Hello ' + name)


say_hello('Hello')


#  if arg is not passed, passing default value

def say_hello(name='Default'):
    print('Hello ' + name)


say_hello()


# prints Hello Default


# return keyword

def add_num(num1, num2):
    return num1 + num2


result = add_num(1, 2)
print(result)


def even_num(num):
    if (num % 2 == 0):
        return True
    else:
        return False


print(even_num(2))

listNum = [1, 1, 1, 3]


def check_even_in_list(listNum):
    for num in listNum:
        print(num)
        if num % 2 == 0:
            return True
        return False # important if all odd numbers

print(check_even_in_list(listNum))
