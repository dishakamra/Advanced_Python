'''
# this example is without @property

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

c = Circle(5)
print(c.radius) # 5
c.area = math.pi * c.radius ** 2
print(c.area) # you want area computed from radius

'''
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius # use _radius internally
    
    @property
    def radius(self):
        """ Radius property"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area) # you want area computed from radius

c.radius = 10
print(c.area)

c.radius = -5