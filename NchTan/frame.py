"""in this code file we implement a way to save
the n choice and t answer quetions and we create
some logics to work with them"""

from __future__ import annotations



class NchTanQ:
    """NchTanQ"""

    question_title: str
    choices: list | set | tuple
    answers: list | set | tuple
    hints: str
    descriptions: str

    def __init__(self,question_title: str,
                      choices: list | set | tuple,
                      answers: list | set | tuple,
                      hints: str="",
                      descriptions: str=""):
        pass

    @staticmethod
    def is_each_item_in_arr(array_1: list | set | tuple,
                            array_2: list | set | tuple):
        """this array  will check if each item in array_1 is in
         array_2 or no"""

        for array_1_item in array_1:
            if array_1_item not in array_2:
                return False

        return True















