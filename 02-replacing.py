import unittest
import pytest


class MySystem:
    def __init__(self):
        self.value = 42

    def increment(self):
        self.value += 1

    def __str__(self):
        return f"MySystem: {self.value}"


class MySystemTest(unittest.TestCase):
    def setUp(self):
        self.system = MySystem()

    def test_str(self):
        self.assertEqual(str(self.system), "MySystem: 42")

    def test_increment(self):
        self.system.increment()
        self.assertEqual(str(self.system), "MySystem: 43")


def test_str(my_system):
    assert str(my_system) == "MySystem: 42"


def test_increment(my_system):
    my_system.increment()
    assert str(my_system) == "MySystem: 43"


@pytest.fixture
def my_system():
    return MySystem()
