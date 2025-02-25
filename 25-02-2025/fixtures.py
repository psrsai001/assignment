import pytest


@pytest.fixture
def data():
    x = 20
    y = 30
    return (x, y)


def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def test_add(data):
    x, y = data
    assert add(x, y) == x + y


def test_mult(data):
    x, y = data
    assert mult(x, y) == x * y
