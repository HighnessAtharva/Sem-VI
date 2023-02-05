# Write a python program to create a class Circle and compute the Area and the circumferences of the circle.(use parameterized constructor)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle: {3.14 * self.radius ** 2}")

    def circumference(self):
        print(f"Circumference of Circle: {round(2 * 3.14 * self.radius, 2)}")


circle = Circle(5)
circle.area()
circle.circumference()
