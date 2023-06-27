"""this is a code file that implements another way to
make the question statements. So sometimes teachers give
some questions that they look the same, and just their numbers
or some words is changed in these cases we can use this statement
creator to create these kinds of things"""
import random
from inspect import isfunction
from inspect import signature


class RostamState:
    """the frame is the frame for making the questions
    and values_formatting is th list of lists of values for
    putting in the frame to make some sort of statement
    function_solving is a function that get the values and return the
    answer. the number of parameters of the function must be equal to
    the number of values are going to be formatted in  the string"""

    __frame: str

    def __init__(self, frame: str,
                 values_formatting: list,
                 function_solving, is_allowed_same):

        if not isfunction(function_solving):
            raise TypeError("the value given as a function is not a function")
        else:
            sin = signature(function_solving)
            number_arg = len(sin.parameters)
            if number_arg != len(values_formatting):
                raise ValueError("""the number of parameters of function does not 
                match the number values for formatting""")

        self.frame = frame
        self.values_formatting = values_formatting
        self.function_solving = function_solving
        self.__is_allowed_same = is_allowed_same
        self.length = len(self.values_formatting)

    def pick_random(self):

        values = []
        for index in range(self.length):

            value = random.choice(self.values_formatting[index])
            values.append(value)

            if not self.__is_allowed_same:
                self.values_formatting[index].remove(value)
        return values

    def form(self):

        # if one of the values for arguments was length 0 it means it is ended
        if not self.__is_allowed_same:
            for i in self.values_formatting:
                if len(i) == 0:
                    return "NVQ"

        values = self.pick_random()
        frame = self.frame.format(*values)
        answer = self.function_solving(*values)
        return frame, answer
