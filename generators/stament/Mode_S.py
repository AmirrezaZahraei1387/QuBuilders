"""the Mode_S is a kind of statement for making
a question that the statement will have some different conditions.
For, example it can be true or false so the statement mode is true or
false"""
from checker import Check_Length


class ModeState(Check_Length):
    """the statements must be dictionary. the dictionary
    must be like the following:
    [statement_1, statement_2, statement_3, statement_4]
    [mode_1, mode_2, mode_3, mode_4]
    """

    def __init__(self, statements: list, modes: list, is_allowed_same: bool):
        super().__init__(statements, modes, is_allowed_same)  # array_1 is now statements and array_2 is now modes
        self.check_length_save()
        self.modes_in = set(modes)  # modes_in is the all possible modes

    def frame(self):

        if len(self.array_1) == 0:
            return "NVQ"

        return self.pick_random()

