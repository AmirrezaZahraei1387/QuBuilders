
import unittest
from QuBu.NchTan import QuestionDataSaver


class test(unittest.TestCase):

    question = QuestionDataSaver("what is the synonym of stupid?", ["idiot", "donkey"],
                          ["idiot", "donkey", "good", "awsome"],
                          "stupid means some one with unruly behaviors",
                          "this is for testing the vocab of students")

    def test_instanting(self):

        try:
            qu = QuestionDataSaver("what is the synonym of stupid?", ["idiot", "donkey"],
                              ["idiot", "donkey", "good", "awsome"],
                              "stupid means some one with unruly behaviors",
                              "this is for testing the vocab of students")
        except ValueError:
            b = False
        else:
            b= True

        self.assertEqual(b, True)

    def test_is_each_item_in_array(self):

        b = self.question.is_each_item_in_arr(self.question.answers, self.question.choices)
        self.assertEqual(b, True)

    def test_is_present(self):

        try:
            self.question.is_present(self.question.choices, self.question.answers, "choices", "answers")
        except ValueError:
            b = True
        else:
            b = False

        self.assertEqual(b, True)


if __name__ == '__main__':
    unittest.main()




