# Write a python script to create a class Rectangle with data member’s length, width and methods area, perimeter which can compute the area and perimeter of rectangle.
 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of the Rectange is {self.length * self.width} sq. units") 

    def perimeter(self):
        print(f"Perimeter of the Rectange is { 2 * (self.length + self.width)} units")
    

r1 = Rectangle(10, 20)
r1.area()
r1.perimeter()
    