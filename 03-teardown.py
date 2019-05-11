import unittest
import pytest


class TestFiles(unittest.TestCase):
    def setUp(self):
        self.file1 = open("01-junit.py")
        self.file2 = open("02-replacing.py")

    def tearDown(self):
        self.file2.close()
        self.file1.close()

    def test_line_count(self):
        count1 = len(self.file1.readlines())
        count2 = len(self.file2.readlines())
        assert count2 > count1


def test_line_count(file1, file2):
    count1 = len(file1.readlines())
    count2 = len(file2.readlines())
    assert count2 > count1


@pytest.fixture
def file1():
    with open("01-junit.py") as f:
        yield f


@pytest.fixture
def file2():
    # If there's no context manager, you can be more verbose:
    f = open("02-replacing.py")
    try:
        yield f
    finally:
        f.close()
