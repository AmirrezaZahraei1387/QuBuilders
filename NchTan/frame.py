"""in this code file we implement a way to save
the n choice and t answer quetions and we create
some logics to work with them"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class QuestionDataSaver:
    question_title: str
    choices: list | set | tuple
    answers: list | set | tuple
    hints: str
    descriptions: str


class NchTanQ(QuestionDataSaver):
    """NchTanQ"""

    question_title: str
    choices: list | set | tuple
    answers: list | set | tuple
    hints: str
    descriptions: str
    number_choices:int

    def __init__(self, question_title: str,
                 choices: list | set | tuple,
                 answers: list | set | tuple,
                 hints: str = "",
                 descriptions: str = ""):

        if not self.is_each_item_in_arr(answers, choices):
            raise ValueError("the answers must be present in  choices")

        super().__init__(question_title, choices,
                         answers, hints, descriptions, len(choices))

    @staticmethod
    def is_each_item_in_arr(array_1: list | set | tuple,
                            array_2: list | set | tuple):
        """this array  will check if each item in array_1 is in
         array_2 or no"""

        for array_1_item in array_1:
            if array_1_item not in array_2:
                return False

        return True

    def __str__(self):

        complete_question = ""
        complete_question += self.question_title

        for choice in self.choices:
            complete_question += '\n'+str(choice)

        complete_question += '\n'+str(self.answers)

        complete_question += '\n'+self.hints
        complete_question += '\n'+self.descriptions

        return complete_question




