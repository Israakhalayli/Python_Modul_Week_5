class Rectangle:

     def __init__(self, width, height):
        self.width = width
        self.height = height
     def area(self):
        return self.width * self.height
     
     def perimeter(self):
         return 2 * (self.width + self.height)
     

my_rectangle = Rectangle(5, 7)

print("Area:", my_rectangle.area())
print("Perimeter:", my_rectangle.perimeter())