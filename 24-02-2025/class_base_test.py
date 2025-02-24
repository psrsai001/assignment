from math import pi
from typing import Callable

from shape import Circle


class TestCircle:
    # run before every test
    def setup_method(self, method: Callable):
        print(f"setting up  {method.__name__}")
        self.circle = Circle(20)

    # run after efery test
    def teardown_method(self, method: Callable):
        print(f"tearing dowin {method.__name__}")

    def test_radius(self):
        assert self.circle.radius == 20

    def test_perimeter(self):
        assert self.circle.perimeter() == pi * self.circle.radius * 2

    def test_area(self):
        assert self.circle.area() == pi * self.circle.radius**2
