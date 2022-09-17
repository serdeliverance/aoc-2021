import unittest
from src.day_02_part_2 import solution


class Day02Par2Test(unittest.TestCase):

    def test(self):
        commands = [("forward", 5),
                    ("down", 5),
                    ("forward", 8),
                    ("up", 3),
                    ("down", 8),
                    ("forward", 2)]
        result = solution(commands)
        self.assertEqual(900, result)
