
from __future__ import annotations
import random


class QuestionDataSaver():

    def __init__(self, question_title: str,
                 answers: list | set | tuple,
                 choices: list | set | tuple,
                 hints: str = "",
                 descriptions: str = ""):

        self.is_present(answers, choices, "answers", "choices")
        self.question_title = question_title
        self.choices = choices
        self.answers = answers
        self.hints = hints
        self.descriptions = descriptions

    @staticmethod
    def is_each_item_in_arr(array_1: list | set | tuple,
                            array_2: list | set | tuple):
        """this array  will check if each item in array_1 is in
        array_2 or no"""

        for array_1_item in array_1:
            if array_1_item not in array_2:
                return False
        return True

    def is_present(self, array_1: list | set | tuple,
                   array_2: list | set | tuple, name_1: str, name_2: str):

        message = "the {} must be present in {}".format(name_1, name_2)

        if not self.is_each_item_in_arr(array_1, array_2):
            raise ValueError(message)

    def shuffle_choices(self):
        """this method shuffle the choices if it is
        needed"""
        random.shuffle(self.choices)
