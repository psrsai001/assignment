import pytest

fruits = ["apple", "banana", "carrot"]


@pytest.fixture(params=fruits)
def fruit(request: pytest.FixtureRequest):
    return request.param


@pytest.fixture(autouse=True)
def log(request: pytest.FixtureRequest):
    print(f"\n[log] funtcion: {request.node.name}")


def test_fruits(fruit):
    assert fruit in fruits
