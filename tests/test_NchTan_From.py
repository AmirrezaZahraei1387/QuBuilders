
import unittest
from NchTan import QuestionDataSaver


class test(unittest.TestCase):

    a = QuestionDataSaver("what is the synonym of stupid?", ["idiot", "donkey"],
                          ["idiot", "donkey", "good", "awsome"],
                          "stupid means some one with unruly behaviors",
                          "this is for testing the vocab of students")

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

    def test_is_each_item_in_array(self):

        b = self.a.is_each_item_in_arr(self.a.answers, self.a.choices)
        self.assertEqual(b, True)

    def test_is_present(self):

        try:
            self.a.is_present(self.a.choices, self.a.answers, "choices", "answers")
        except ValueError:
            b = True
        else:
            b = True

        self.assertEqual(b, True)


if __name__ == '__main__':
    test.main()




