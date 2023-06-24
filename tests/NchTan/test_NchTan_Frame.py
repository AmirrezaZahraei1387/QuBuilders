
from NchTan import NchTanQ
import unittest


class test(unittest.TestCase):

    a = NchTanQ("what is the synonym of stupid?", ["idiot", "donkey"],
                          ["idiot", "donkey", "good", "awsome"],
                          "stupid means some one with unruly behaviors",
                          "this is for testing the vocab of students")

    def test___eq__(self):

        b = self.a == ["idiot", "donkey"]
        self.assertEqual(b, True)

    def test___req__(self):

        try:
            b = self.a == ["go"]
        except ValueError:
            c = True
        else:
            c = False

        self.assertEqual(c, True)


if __name__ == "__main__":
    unittest.main()


