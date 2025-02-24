from shape import Rect


def test_area():
    rect = Rect(20, 20)
    assert rect.area() == 20 * 20


def test_perimeter():
    rect = Rect(20, 20)
    assert rect.perimeter() == 2 * (20 + 20)
