"""the Mode_S is a kind of statement for making
a question that the statement will have some different conditions.
For, example it can be true or false so the statement mode is true or
false"""
import random


class ModeState:
    """the statements must be dictionary. the dictionary
    must be like the following:
    [statement_1, statement_2, statement_3, statement_4]
    [mode_1, mode_2, mode_3, mode_4]
    """

    def __init__(self, statements: list, modes: list, is_allowed_same: bool):
        self.statements = statements
        self.modes = modes  # these modes are the modes of each statement
        self.modes_in = set(self.modes)  # modes_in is the all possible modes
        self.is_allowed_same = is_allowed_same





