"""this is a code file that is created to write
the questions in a json file or in a sequence of json files
inside a folder.
the folder however must have the following format otherwise
there will be an error:
dir_name
|
|___question_1.json
|___question_2.json
|___question_3.json
|___question_4.json
|..."""
import NchTan
from type_checker import check_type_question
import json
import os


@check_type_question(NchTan.QuestionDataSaver)
def write_file(question, file_object):
    json_obj = {
        "question_title": question.question_title,
        "answers": question.answers,
        "choices": question.choices,
        "hints": question.hints,
        "descriptions": question.descriptions
    }

    json.dump(json_obj, file_object)

    file_object.close()


@check_type_question(NchTan.QuSeq)
def write_files_all(questions, directory: str):
    files_paths = os.listdir(directory)
    if len(files_paths) != len(questions):
        raise ValueError("the number of files and questions are not equal")

    index = -1
    for path in files_paths:
        index += 1
        write_file(questions[index], open(directory + path, 'w'))
