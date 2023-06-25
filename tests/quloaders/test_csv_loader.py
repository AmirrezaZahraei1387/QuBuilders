from quloaders import csv_loader
import unittest


class test(unittest.TestCase):

    def test_read_file(self):
        file = open("data_sample/exam.csv", 'r', encoding='utf-8')
        qus = csv_loader.read_file(file, "hello", "the hello")
        self.assertEqual(qus[0].choices, [12, 11, 45, 7])  # it checks if the choices of question  1 is the same as
        # expected or no


if __name__ == "__main__":
    unittest.main()
