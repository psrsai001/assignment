import pytest

"""
We have seen in fixtures.py file if we want to log the function that is 
running currently without returning any value we can do autouse 
it will use the fixture before every test.
"""


@pytest.fixture(autouse=True)
def log_function(request: pytest.FixtureRequest):
    print(f"\n\nrunning {request.node.name}\n\n")


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
