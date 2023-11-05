#area and perimeter of a rectangle
class Rectangle:
    def __init__(self):
        self.length = int(input("Enter the length of the rectangle: "))
        self.width = int(input("Enter the width of the rectangle: "))

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
my_rectangle = Rectangle()

print("Area: " + str(my_rectangle.area()))
print("Perimeter: " + str(my_rectangle.perimeter()))

