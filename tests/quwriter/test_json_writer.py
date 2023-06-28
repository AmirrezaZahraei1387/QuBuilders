import unittest
from quwriter import json_writer
from NchTan import QuestionDataSaver
from quloaders import pas

class test(unittest.TestCase):

    def test_write_single(self):
        PATH = "data_sample/eq/exa.json"
        file = open(PATH, 'w')
        question = QuestionDataSaver("what is 5+6?", ["11"], ["11", "12", "13", "14"])
        json_writer.write_file(question, file)


