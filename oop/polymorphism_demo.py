import math

class Shape:
    def area(self):
        """
        The base class method raises NotImplementedError to ensure that this method is overridden by the derived classes.
        """
        raise NotImplementedError("Subclasses should implement this method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Overriding the area() method to calculate the area of a rectangle.
        Formula: length × width
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Overriding the area() method to calculate the area of a circle.
        Formula: π × radius²
        """
        return math.pi * (self.radius ** 2)
