from math import pi


class Shape:
    def perimeter(self):
        raise NotImplementedError("Subclasses must override perimeter()")

    def area(self):
        raise NotImplementedError("Subclasses must override area()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius**2


class Rect(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rect):
            return False
        return self.width == other.width and self.height == other.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height
