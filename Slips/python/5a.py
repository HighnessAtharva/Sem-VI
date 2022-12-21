# Write an anonymous function to find area of square and rectangle.

area_of_square=lambda x: x**2
x=float(input("Enter the length of the square: "))
print(f"Area of the square is: {area_of_square(x)} sq. units")

area_of_rectangle=lambda x,y: x*y
x=float(input("Enter the length of the rectangle: "))
y=float(input("Enter the breadth of the rectangle: "))
print(f"Area of the rectangle is: {area_of_rectangle(x,y)} sq. units")