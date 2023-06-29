import unittest
from generators.stament import AsgharState


class test(unittest.TestCase):

    def test_check_init_1(self):

        try:
            AsgharState(["ffff", "gggggg"], ["ffff", "gggggg"], "KEY", True)
        except ValueError:  # if something else rather than KEY or VALUE is given to class it must
            # raise an error
            a = False
        else:
            a = True
        self.assertEqual(a, True)

    def test_check_init_2(self):

        try:
            AsgharState(["ffff", "gggggg"], ["ffff", "gggggg"], "KEYe", True)
        except ValueError:  # if something else rather than KEY or VALUE is given to class it must
            # raise an error. for example like here
            a = True
        else:
            a = False

        self.assertEqual(a, True)

    def test_NVQ(self):

        obj = AsgharState(["and", "hello"], ["et", "bonjour"], "KEY", False)
        obj.frame = "what is {} in french?"
        for i in range(7):
            a = obj.frame
        self.assertEqual(a, "NVQ")  # because we said that the is_allowed_same is False so that it must print NVQ
        # after two iterations


if __name__ == "__main__":
    unittest.main()
