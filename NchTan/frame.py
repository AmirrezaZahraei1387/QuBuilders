"""in this code file we implement a way to save
the n choice and t answer questions, and we create
some logics to work with them"""

from __future__ import annotations
from form import QuestionDataSaver


class NchTanQ(QuestionDataSaver):
    """NchTanQ"""

    def __str__(self):

        complete_question = ""
        complete_question += self.question_title

        for choice in self.choices:
            complete_question += '\n' + str(choice)

        complete_question += '\n' + str(self.answers)

        complete_question += '\n' + self.hints
        complete_question += '\n' + self.descriptions

        return complete_question

    def __eq__(self, other: list | set | tuple):

        self.is_present(other, self.choices, "your answer", "choices")
        return self.is_each_item_in_arr(self.answers, other)

    def __req__(self, other: list | set | tuple):
        self.is_present(other, self.choices, "your answer", "choices")
        return self.is_each_item_in_arr(self.answers, other)

