import unittest
from quwriter import json_writer
from NchTan import QuestionDataSaver
from NchTan import QuSeq
from quloaders import read_file_j, read_all_files_j

question = QuestionDataSaver("what is 5+6?", ["11"], ["11", "12", "13", "14"])
question_2 = QuestionDataSaver("what is 4+7?", ["11"], ["11", "5", "4", "3", "2"], "hhhh", "kkkk")
questions = QuSeq()
questions += question
questions += question_2


class test(unittest.TestCase):

    def test_write_single(self):
        PATH = "data_sample/eq/exa.json"

        # here we write the file
        file = open(PATH, 'w')

        json_writer.write_file(question, file)
        file.close()

        # here we read the file
        file = open(PATH, 'r')
        qu = read_file_j(file)
        file.close()
        self.assertEqual(qu.answers, question.answers) # if the answers of the question  in the
        # is equal to the answers of the question we have here we assume that the function works correctly

    def test_write_all(self):

        # we wrote the questions inside the directory
        PATH = "data_sample/eq/"
        json_writer.write_files_all(questions, PATH)
        # now in order to check if every thing is written correctly we load the file and check it
        qus = read_all_files_j(PATH, "", "")
        self.assertEqual(qus[0].answers, ["11"])
        # if the question number 1 in question sequence object has the same answers with the question we wrote
        # we assume that it works correctly


if __name__ == "__main__":
    unittest.main()

