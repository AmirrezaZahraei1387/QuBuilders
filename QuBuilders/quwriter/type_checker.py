
from __future__ import annotations


def check_type_question(type_):
    """this function will add the ability of checking."""
    def checker(function):
        def new_function(obj_question: type_, file_obj):
            if not isinstance(obj_question, type_):
                raise TypeError("the type of the given object must be (NchTan.QuestionDataSaver, NchTan.QuSeq).")

            return function(obj_question, file_obj)
        return new_function
    return checker



