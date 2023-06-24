from QuBu.NchTan import QuSeq
from QuBu.NchTan import QuestionDataSaver
import unittest

# creating a QuSeq object
question_1 = QuestionDataSaver("what is the synonym of stupid?", ["idiot", "donkey"],
                               ["idiot", "donkey", "good", "awsome"],
                               "stupid means some one with unruly behaviors",
                               "this is for testing the vocab of students")

question_2 = QuestionDataSaver("what is the synonym of stupid?", ["idiot", "donkey", "goat"],
                               ["idiot", "donkey", "good", "awsome", "goat"],
                               "stupid means some one with unruly behaviors",
                               "this is for testing the vocab of students")

question_3 = QuestionDataSaver("what is the synonym of stupid?", ["idiot", "donkey", "goat"],
                               ["idiot", "donkey", "good", "awsome", "goat"],
                               "stupid means some one with unruly behaviors",
                               "this is for testing the vocab of students")

question_4 = QuestionDataSaver("what is the synonym of stupid?", ["idiot", "donkey", "goat"],
                               ["idiot", "donkey", "good", "awsome", "goat"],
                               "stupid means some one with unruly behaviors",
                               "this is for testing the vocab of students")

questions = QuSeq("my questions", "some questions for students")
questions += question_1
questions += question_2
questions += question_3


class test(unittest.TestCase):

    def test_adding(self):
        global questions
        try:
            questions += question_4
        except TypeError:
            a = False
        else:
            a = True

        self.assertEqual(a, True)

    def test_get_item(self):

        a = questions[1].answers
        self.assertEqual(a, ["idiot", "donkey", "goat"])

    def test_len(self):

        a = len(questions)
        self.assertEqual(a, 4)


if __name__ == "__main__":
    unittest.main()



