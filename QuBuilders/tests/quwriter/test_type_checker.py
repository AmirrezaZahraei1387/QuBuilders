import unittest
from QuBuilders.quwriter import check_type_question


class test(unittest.TestCase):

    def test_check_type_question_1(self):
        """check if the given type will be checked for
        the first arg"""

        # it must raise an error if num_1 was not actually int
        @check_type_question(int)
        def add(number_1: int, number_2: float):
            return number_1 + number_2

        try:
            add(3.6, 34)  # raise an error because num_1 is not int
        except TypeError:
            b = True
        else:
            b = False

        self.assertEqual(b, True)

    def test_check_type_question_2(self):
        # it must raise an error if num_1 was not actually int
        @check_type_question(int)
        def add(number_1: int, number_2: float):
            return number_1 + number_2

        try:
            add(4, 7)  # no error because number_1 is integer
        except TypeError:
            a = False
        else:
            a = True

        self.assertEqual(a, True)


if __name__ == "__main__":
    unittest.main()