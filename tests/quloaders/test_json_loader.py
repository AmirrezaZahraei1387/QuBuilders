import quloaders
import unittest


class test(unittest.TestCase):

    def test_read_file(self):
        file = open("data_sample/eq/exa.json", 'r', encoding="utf-8")
        qu = quloaders.read_file(file_object=file)
        self.assertEqual(qu.answers == ["adison"], True)  # checking if the answer of the question will be true



if __name__ == "__main__":
    unittest.main()
