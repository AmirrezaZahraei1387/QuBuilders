"""this the writer that write question sequence or
a single question inside a csv file. the header of the
csv will be:
question_title; answers; choices; hints; descriptions
 and the delimiter of csv file is ;"""

from QuBuilders.quwriter.type_checker import check_type_question
from QuBuilders import NchTan
import csv


@check_type_question(type_=NchTan.QuSeq)
def csv_write(obj_question, file_obj):

    writer = csv.writer(file_obj)
    for question in obj_question:
        assert isinstance(question, NchTan.QuestionDataSaver)
        writer.writerow([question.question_title,
                         question.answers,
                         question.choices,
                         question.hints,
                         question.descriptions])

    file_obj.close()
