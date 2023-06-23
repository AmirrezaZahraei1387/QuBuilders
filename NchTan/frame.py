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
    def is_each_item_in_arr():
        pass














