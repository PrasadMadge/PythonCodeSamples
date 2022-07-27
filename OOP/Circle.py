class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.pi * self.radius * self.radius

myCircle = Circle(6)
print(myCircle.pi)
print(myCircle.radius)
print(myCircle.area())
