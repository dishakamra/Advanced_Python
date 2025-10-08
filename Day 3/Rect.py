# Write a Rectangle with width and height. Add an instance method area() that returns width * height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
print(r.area()) # 12