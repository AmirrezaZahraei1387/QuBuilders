
import unittest
from NchTan import QuestionDataSaver


class test(unittest.TestCase):

    def test_instanting(self):

        try:
            a = QuestionDataSaver("what is the synonym of stupid?", ["idiot", "donkey"],
                              ["idiot", "donkey", "good", "awsome"],
                              "stupid means some one with unruly behaviors",
                              "this is for testing the vocab of students")
        except ValueError:
            b = False
        else:
            b= True

        self.assertEqual(b, True)

