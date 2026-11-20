from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self,name):
        self._name = name #protected

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print(f"{self._name} has area {self.area():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
"""
circle = Circle(5)
rectangle = Rectangle(4, 6)
circle.describe()  # Output: Circle has area 78.54
rectangle.describe()  # Output: Rectangle has area 24.00
"""

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    shape.describe()  # Output: Circle has area 78.54, Rectangle has area 24.00