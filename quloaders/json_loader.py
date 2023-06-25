"""this is file that is created to load the
questions that are saved with json files.
so the questions must be organized like
the following.

question.json

{
  "question_title": "",
  "answers": ["", "", ... ],
  "choices": ["", "", ... ],
  "hints": "",
  "descriptions": ""
}"""

import json
from NchTan import QuSeq, QuestionDataSaver
import os


def read_file(file_object):
    data = json.load(file_object)
    question = QuestionDataSaver(data["question_title"],
                                 data["answers"],
                                 data["choices"],
                                 data["hints"],
                                 data["descriptions"])
    return question


def read_all_files(path_directory: str, name: str, des: str):
    """this function will read all the json files in a directory.
    the file_object is the file you should open and give.
    the name is the name of your question sequence and des
    is its descriptions"""

    files = os.listdir(path_directory)
    seq = QuSeq(name, des)

    for ra_path in files:
        path = path_directory+ra_path
        qu = read_file(open(path, "r"))
        seq += qu

    return seq


















