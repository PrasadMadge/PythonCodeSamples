# *args, treats it as a tuples of paramentrs that are coming

def myfunc(*args):
    print(args)  # (1, 2, 3) , returns tuple
    for item in args:
        print(item)
    return sum(args)


print(myfunc(1, 2, 3))


#  kwargs, key value pair dictonaries

def myfunc1(**kwargs):
    print(kwargs) # {'fruit': 'apple', 'veggie': 'potato'} , return dict
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('not found')


mydict1 = {'fruit': 'apple', 'veggie': 'potato'}
myfunc1(fruit='apple', veggie='potato')


# combo of both

def myfunc2 (*args, **kwargs):
    print(args)
    print(kwargs)

myfunc2(10,20,30, key1 = 'value1' , key2 = 'value2')