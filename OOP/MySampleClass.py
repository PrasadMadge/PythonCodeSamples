# self pass in many methods.
# in many oops programming langs , self obj is hiddenly passed.
# in python it is passed and mentioned explicitly


class MySample:
    def func(self):
        pass

    def __init__(self):
        print('Sample obj intialized')


my_sample = MySample()
print(type(my_sample))


class Dog():

    # adding a attribute which is same across all object instances
    species = 'mammal'

    def __init__(self, breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print('Woof ! , my name is {} and number is {}'.format(self.name, number))
#         imp, number is not using self but name is

dog = Dog(breed='pug',name='Tobi', spots='2')
# or dog = Dog(breed = 'pug') or Dog('pug')
print(dog.breed)
print(dog.name)
print(dog.spots)
print(dog.species)

dog.bark(8)