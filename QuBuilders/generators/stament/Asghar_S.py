"""the Asghar_S is a statement generator for questions
that will work as the following:
so first it neads a frame so the frame is going to be
given from the user or anyone using the code. For example
frame can be like the following.
What is {} in Farsi?"""
from QuBuilders.generators.stament.checker import Check_Length


class AsgharState(Check_Length):
    """mode defines from keys or values we should pick.
    key means key
    value means value"""
    __Frame: str = ""
    statement_coms: list
    statement_keys: list
    length: int

    def __init__(self, statement_coms: list, statement_keys: list, mode: str, is_allowed_same: bool):

        if mode.lower() == "key":
            super().__init__(statement_coms, statement_keys, is_allowed_same)
        elif mode.lower() == "value":
            super().__init__(statement_keys, statement_coms, is_allowed_same)
        else:
            raise ValueError("the mode can only be value or key given " + str(mode))

        self.check_length_save()

    @property
    def frame(self):

        if len(self.array_1) == 0:
            return "NVQ"

        statement_com, statement_key = self.pick_random()

        frame_state = self.__Frame.format(*statement_com)
        return frame_state, statement_key

    @frame.setter
    def frame(self, frame_: str):
        self.__Frame = frame_
