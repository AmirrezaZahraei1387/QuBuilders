"""here in this code file we implement a way to
save a sequence of questions with class. name and give different
descriptions for them. The question sequence is just something to save
more than one question but in a way to manage it better."""

import random
from QuBuilders.NchTan.form import QuestionDataSaver


class QuSeq:
    """QuSeq"""

    def __init__(self, name_quseq: str= "", descriptions_quseq: str= ""):
        self.name_QuSeq = name_quseq
        self.descriptions_QuSeq = descriptions_quseq
        self.__questions = []

    def __iadd__(self, question: QuestionDataSaver):

        if not isinstance(question, QuestionDataSaver):
            raise TypeError("the given object is not QuestionDataSaver object.")
        self.__questions.append(question)

        return self

    def __getitem__(self, key: int):
        return self.__questions[key]

    def shuffle_questions_seq(self):
        random.shuffle(self.__questions)

    def __len__(self):
        return len(self.__questions)

    def shuffle_questions_choices_f(self, iter_times: int):
        """this method will shuffle the questions choices.
        so first you specify the times we need to iter by passing
        a value to iter_times then we make a random number each for the
        index, and we shuffle the questions of that index"""

        for i in range(iter_times):

            index = random.randint(0, len(self)-1)
            # all the items of __questions must be an instance of class QuestionDataSaver
            assert isinstance(self[index], QuestionDataSaver)
            self[index].shuffle_choices()

    def shuffle_questions_choices_a(self):
        """this method will shuffle all the choices of the given
        questions"""

        for index in range(len(self)):

            assert isinstance(self[index], QuestionDataSaver)
            # all the items of __questions must be an instance of class QuestionDataSaver
            self[index].shuffle_choices()
