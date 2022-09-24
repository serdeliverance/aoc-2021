import unittest
from src.day_03a import solution


class Day03Part1Test(unittest.TestCase):

    def test(self):
        input = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010"
        ]

        result = solution(input)
        self.assertEqual(198, result)
