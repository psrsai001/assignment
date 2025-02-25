from io import TextIOWrapper

import pytest

"""
Assume you have to log all the tests that run during the execution in a file
called "log.txt".

Without fixtures we have to open and close the file everytime we write the test

With fixtures we can define a module(file) level fixture that can used when the
current python file is running.

by using yield we can also perform cleanups
"""


@pytest.fixture(scope="module")
def file():
    print("Module Scope: opening the file for others to write")
    with open("log.txt", "w") as f:
        yield f
    print("Module Scope: closed the file")


def test_1(file: TextIOWrapper):
    print("testing 1")
    file.write("running test 1\n")
    assert True


def test_2(file: TextIOWrapper):
    print("testing 2")
    file.write("running test2\n")
    assert True
