"""the Asghar_S is a statement generator for questions
that will work as the following:
so first it neads a frame so the frame is going to be
given from the user or anyone using the code. For example
frame can be like the following.
What is {} in Farsi?
Afterward the code will need a data like the following:
{("hello"):["salam"], ("how are you"):["khobi"], ("goodbye"): ["khoda hafez"]}
then you have to say from which part(keys or values) we should pick"""
import random

class State:
    """mode defines from keys or values we should pick.
    key means key
    value means value"""
    __Frame: str
    statement_coms: list
    statement_keys: list

    def __init__(self, data_question: dict, mode: str):
        def save(value_1, value_2):
            """this is a method that is created to give a same value in
            different ways to two vars"""
            self.statement_coms = list(value_1)
            self.statement_keys = list(value_2)

        if mode.lower() == "key":
            save(data_question.keys(), data_question.values())

        elif mode.lower() == "value":
            save(data_question.values(), data_question.keys())

        else:
            raise ValueError("the mode can only be value or key given "+str(mode))

        if not (len(self.statement_keys) == len(self.statement_coms)):
            raise ValueError("the length of keys and values of the data didn't match")

    @property
    def frame(self):

        statement_key = random.choice(self.statement_keys)



    @frame.setter
    def frame(self, frame: str):
        self.__Frame = frame













