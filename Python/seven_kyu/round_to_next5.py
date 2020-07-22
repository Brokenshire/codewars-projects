# Python solution for 'Round up to the next multiple of 5' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS
# Author: Jack Brokenshire
# Date: 22/07/2020

import unittest
import math


def round_to_next5(n):
    """
    Given an integer as input, can you round it to the next (meaning, "higher") 5?
    :param n: integer input.
    :return: always round integer n up to nearest multiple of 5.
    """
    return math.ceil(n / 5) * 5


class TestRoundToNext5(unittest.TestCase):
    """Class to test 'round_to_next5' function"""

    def test_round_to_next5(self):
        inp = 0
        out = round_to_next5(inp)
        self.assertEqual(out, 0, "Input: {}".format(inp))

        inp = 1
        out = round_to_next5(inp)
        self.assertEqual(out, 5, "Input: {}".format(inp))

        inp = -1
        out = round_to_next5(inp)
        self.assertEqual(out, 0, "Input: {}".format(inp))

        inp = 5
        out = round_to_next5(inp)
        self.assertEqual(out, 5, "Input: {}".format(inp))

        inp = 7
        out = round_to_next5(inp)
        self.assertEqual(out, 10, "Input: {}".format(inp))

        inp = 20
        out = round_to_next5(inp)
        self.assertEqual(out, 20, "Input: {}".format(inp))

        inp = 39
        out = round_to_next5(inp)
        self.assertEqual(out, 40, "Input: {}".format(inp))


if __name__ == '__main__':
    unittest.main()
