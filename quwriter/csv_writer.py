"""this the writer that write question sequence or
a single question inside a csv file. the header of the
csv will be:
question_title; answers; choices; hints; descriptions
 and the delimiter of csv file is ;"""
from __future__ import annotations
from type_checker import check_type_question
import NchTan


@check_type_question
def write(obj_question: NchTan.QuestionDataSaver| NchTan.QuSeq):
    pass



