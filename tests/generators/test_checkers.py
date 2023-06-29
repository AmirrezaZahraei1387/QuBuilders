import unittest
from generators.stament import Check_Length


class test(unittest.TestCase):

    def test_instantinating(self):

        try:
            Check_Length([0, 6, 3, 2, 2], [7, 4, 2, 1, 1], True)
        except Exception:  # it means that there is an error with __init__
            a = False
        else:  # it means there is no error with the __init__
            a = True

        self.assertEqual(a, True)

    def test_length_save(self):
        obj = Check_Length([0, 6, 3, 2, 2], [7, 4, 2, 1, 1], True)
        try:
            obj.check_length_save()
        except ValueError:
            a = False
        else:
            a = True

        self.assertEqual(a, True)

    def pick_random_removing(self):
        obj = Check_Length([0, 6, 3, 2], [7, 4, 2, 1], False)
        a, b = obj.pick_random()
        self.assertEqual(a in obj.array_1, False)


if __name__ == "__main__":
    unittest.TestCase()




