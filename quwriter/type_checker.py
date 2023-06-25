
from __future__ import annotations
import NchTan


def check_type_question(function):
    """this function will add the ability of checking """
    def new_function(obj_question: NchTan.QuestionDataSaver| NchTan.QuSeq):
        if not isinstance(obj_question, (NchTan.QuestionDataSaver, NchTan.QuSeq)):
            raise TypeError("the type of the given object must be (NchTan.QuestionDataSaver, NchTan.QuSeq).")

        return function(obj_question)

