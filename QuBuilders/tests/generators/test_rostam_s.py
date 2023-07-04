import unittest
from QuBuilders.generators.stament import RostamState


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

        def add__(a, b, c):
            return a+b+c

        try:
            RostamState("what is {}+{}?", [[5, 3, 2, 1, 4], [5, 3, 2, 1, 4]], add__, False)
        except ValueError:
            y = True
        else:
            y = False

        self.assertEqual(y, True)

    def test_check_length(self):
        """the check_length will check if all the given
        arrays have the same length or no"""
        def add(a, b):
            return a + b

        obj = RostamState("what is {}+{}?", [[5, 3, 2, 8, 4], [5, 3, 2, 1, 4]], add, False)

        try:
            obj.check_lengths()
        except ValueError:
            v = False
        else:
            v = True    # no error because all the given arrays have the same length

        self.assertEqual(v, True)

    def test_form_NVQ(self):
        """if the value of is_allowed_same was specified to False
        after all the data was used the form function just
        give NVQ"""

        def add(a, b):
            return a + b

        obj = RostamState("what is {}+{}?", [[5, 3, 2, 8, 4], [5, 3, 2, 1, 4]], add, False)

        for i in range(6):
            a = obj.form()
        self.assertEqual(a, "NVQ")

    def test_pick_random(self):
        """if we specify the value of is_allowed_same the class will
        automatically remove the data that is used. Now here we
        receive some random data, and then we check if it exists or no."""
        def add(a, b):
            return a + b

        obj = RostamState("what is {}+{}?", [[5, 3, 2, 8, 4], [5, 3, 2, 1, 4]], add, False)

        length = len(obj.values_formatting[0])
        obj.pick_random()
        length_new = len(obj.values_formatting[0])

        self.assertEqual(length_new + 1, length)    # when the random value is received the values must be removed
        # from the
        # data list. So the length should decrease


if __name__ == "__main__":
    unittest.main()








