import unittest
from src.day_01b import solution


class Day01Par2Test(unittest.TestCase):

    def test(self):
        result = solution([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
        self.assertEqual(5, result)

    def test_length_less_than_window(self):
        result = solution([1, 2, 3])
        self.assertEqual(6, result)
