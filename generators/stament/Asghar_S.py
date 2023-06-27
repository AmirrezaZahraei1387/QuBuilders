"""the Asghar_S is a statement generator for questions
that will work as the following:
so first it neads a frame so the frame is going to be
given from the user or anyone using the code. For example
frame can be like the following.
What is {} in Farsi?
Afterward the code will need a data like the following:
{("hello", ):["salam"], ("how are you", ):["khobi"], ("goodbye", ): ["khoda hafez"]}
then you have to say from which part(keys or values) we should pick
important note: pass the keys as tuples and add a ',' at the end otherwise
unexpected result will come up"""
import random


class check_length:

    length: int

    def __init__(self, array_1: list, array_2: list, is_allowed_same: bool):
        self.array_1 = array_1
        self.array_2 = array_2
        self.__is_allowed_same = is_allowed_same

    def check_length_save(self):
        """this method will check the length of statement_keys and
        statement_coms, and it will save one of them"""
        self.length = len(self.array_1)

        if not (self.length == len(self.array_2)):
            raise ValueError("the length of keys and values of the data didn't match")

    def check_end(self):
        if len(self.array_1) == 0:
            return "NVQ"

    def pick_random(self):

        index = random.randint(0, self.length - 1)
        value_1 = self.array_1[index]
        value_2 = self.array_2[index]

        if not self.__is_allowed_same:
            self.array_1.pop(index)
            self.array_2.pop(index)
            self.length -= 1

        return value_1, value_2


class AsgharState(check_length):
    """mode defines from keys or values we should pick.
    key means key
    value means value"""
    __Frame: str
    statement_coms: list
    statement_keys: list
    length:int

    def __init__(self, data_question: dict, mode: str, is_allowed_same: bool):
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
            raise ValueError("the mode can only be value or key given " + str(mode))

        super().__init__(self.statement_coms, self.statement_keys, self.__is_allowed_same)

        self.check_length_save()

        self.__is_allowed_same = is_allowed_same


    @property
    def frame(self):

        if len(self.statement_keys) == 0:
            return "NVQ"

        statement_com, statement_key = self.pick_random()

        frame_state = self.__Frame.format(*statement_com)
        return frame_state, statement_key

    @frame.setter
    def frame(self, frame: str):
        self.__Frame = frame
