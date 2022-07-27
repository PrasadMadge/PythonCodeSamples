class Car:
    def move(self):
        print('car moves')

    def __init__(self):
        pass

    def stop(self):
        print('car stops')

class Maruti(Car):
    def __init__(self):
        Car.__init__(self)
        print('Maruti created in init')
#         important to see how Parent init is called.

#     overriding an method from parent class
    def move(self):
        print('Moving in Maruti Style')

#         add on new methods too
    def fly(self):
        print('flying in Maruti Style')


maruti = Maruti()
maruti.move()
maruti.stop()
maruti.fly()
# all Parent class methods are accessible
