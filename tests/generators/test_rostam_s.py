import unittest
from generators.stament import RostamState


class test(unittest.TestCase):

    def test_init__1(self):
        """if the value for function was not a function, it should
        raise a TypeError"""
        add = 5
        try:
            RostamState("what is {}+{}?", [[5, 3, 2, 1, 4], [5, 3, 2, 1, 4]], add, False)
        except TypeError:
            a = True
        else:
            a = False

        self.assertEqual(a, True)

    def test_init__2(self):
        """if the number of parameters given to the function
        does match the number of values to format the program
        raise a ValueError"""

        def add(a, b, c):
            return a+b+c

        try:
            RostamState("what is {}+{}?", [[5, 3, 2, 1, 4], [5, 3, 2, 1, 4]], add, False)
        except ValueError:
            y = True
        else:
            y = False

        self.assertEqual(y, True)

    def test_values_formating_func(self):
        pass