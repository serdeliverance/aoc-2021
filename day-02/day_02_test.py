import unittest
from day_02 import solution


class Day02Test(unittest.TestCase):

    def test(self):
        commands = [("forward", 5),
                    ("down", 5),
                    ("forward", 8),
                    ("up", 3),
                    ("down", 8),
                    ("forward", 2)]
        result = solution(commands)
        self.assertEqual(150, result)
