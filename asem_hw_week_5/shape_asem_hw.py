class Shape:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area_calculate(self):
        return self.width * self.height
class Rectangle(Shape):
    def calculate_area(self):
        return  self.width *  self.height
class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)

# Create rectangle
rect = Rectangle(4, 6)
print("Rectangle area:", rect.calculate_area())

# Create square
sq = Square(5)
print("Square area:", sq.area_calculate())