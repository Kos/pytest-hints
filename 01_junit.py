import unittest


def func(arg):
    return arg * 2


class FuncTest(unittest.TestCase):
    def test_func(self):
        assert func(10) == 20
