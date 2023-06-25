"""this the writer that write question sequence or
a single question inside a csv file. the header of the
csv will be:
question_title; answers; choices; hints; descriptions
 and the delimiter of csv file is ;"""

from type_checker import check_type_question
import NchTan
import csv


@check_type_question
def csv_write(obj_question: NchTan.QuSeq,
          file_obj):

    writer = csv.writer(file_obj)
    for question in obj_question:
        assert isinstance(question, NchTan.QuestionDataSaver)
        writer.writerow([question.question_title,
                         question.answers,
                         question.choices,
                         question.hints,
                         question.descriptions])

