import unittest
from src.day_01a import solution


class Day01Test(unittest.TestCase):

    def test(self):
        result = solution([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
        self.assertEqual(7, result)
