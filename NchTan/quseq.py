"""here in this code file we implement a way to
save a sequence of questions with class. name and give different
descriptions for them. The question sequence is just something to save
more than one question but in a way to manage it better."""

from form import QuestionDataSaver

class QuSeq:
    """QuSeq"""

    __questions: list

    def __init__(self, name_quseq: str, descriptions_quseq: str):
        self.name_QuSeq = name_quseq
        self.descriptions_QuSeq = descriptions_quseq

    def __iadd__(self, question):



