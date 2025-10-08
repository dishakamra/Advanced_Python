"""
Create an ABC Shape with abstract method area(). Implement Circle(Shape) and show its area for radius 2.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

print(Circle(2).area())