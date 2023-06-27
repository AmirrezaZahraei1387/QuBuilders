"""in the TF_S and Asghar_S the implementations are a little the same so
in order to avoid writing a lot of similar codes this class
is created."""

import random


class Check_Length:
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

    def pick_random(self):

        index = random.randint(0, self.length - 1)
        value_1 = self.array_1[index]
        value_2 = self.array_2[index]

        if not self.__is_allowed_same:
            self.array_1.pop(index)
            self.array_2.pop(index)
            self.length -= 1

        return value_1, value_2
