import pytest


def add(x, y):
    return x + y


def mult(x, y):
    return x * y


@pytest.mark.ar
def test_add():
    assert add(2, 3) == 5
    assert add(3, 3) == 6


@pytest.mark.ar
def test_mult():
    assert mult(2, 3) == 6


@pytest.mark.smtg
def test_somethin():
    assert True


@pytest.mark.smtg
def test_some_otherthing():
    assert True


@pytest.mark.smtg
def test_some_other_thing():
    assert True
