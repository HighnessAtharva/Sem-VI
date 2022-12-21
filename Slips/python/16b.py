# Define a class named Shape and its subclass Square. The subclass has an init function which takes an argument Length. Both classes should have methods to calculate area and perimeter of a given shape.                                                                       

class Shape:
    def __init__(self, length):
        self.length = length
        
    def area(self):
        print(f"Area of {type(self).__name__}: {self.length ** 2}")
        
    def perimeter(self):
        print(f"Perimeter of {type(self).__name__}: {self.length * 4}")
        
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
    
    def area(self):
        super().area()
        
    def perimeter(self):
        super().perimeter()
        
square = Square(5)
square.area()
square.perimeter()