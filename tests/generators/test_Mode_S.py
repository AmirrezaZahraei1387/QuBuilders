
import unittest
from generators import ModeState


class test(unittest.TestCase):

    def test_instantinating(self):

        try:
            ModeState(["3+7 = 10", "8+6=13", "7+7=23"], ["T", "F", "F"], False)
        except Exception:
            a = False
        else:
            a=True

        self.assertEqual(a, True)

    def test_NVQ_response(self):
        obj = ModeState(["3+7 = 10", "8+6=13", "7+7=23"], ["T", "F", "F"], False)
        for i in range(12):
            q = obj.frame() # after three iterations the answer of this statement must be NVQ

        self.assertEqual(q, "NVQ")

