# Python solution for "Sum of Pairs" codewars question.
# Level: 5 kyu
# Tags: FUNDAMENTALS, PARSING, ALGORITHMS, STRINGS, MEMOIZATION, DESIGN PATTERNS, and DESIGN PRINCIPLES.
# Author: Jack Brokenshire
# Date: 08/04/2020

import unittest


def sum_pairs(ints, s):
    """
    Finds the first pairs to equal the integer given.
    of appearance that add up to form the sum.
    :param ints: list of integers.
    :param s: integer sum value.
    :return: the first two values (parse from the left please) in order of appearance that add up to form the sum.
    """
    seen = set()
    for x in ints:
        if s - x in seen:
            return [s - x, x]
        seen.add(x)


class TestSumPairs(unittest.TestCase):
    """Class to test "sum_pairs" function"""

    def test_sum_pairs(self):
        self.assertEqual(sum_pairs([1, 4, 8, 7, 3, 15], 8), [1, 7])
        # Basic: %s should return [1, 7] for sum = 8
        self.assertEqual(sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])
        # Negatives: %s should return [0, -6] for sum = -6
        self.assertEqual(sum_pairs([20, -13, 40], -7), None)
        # No Match: %s should return None for sum = -7
        self.assertEqual(sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1])
        # First Match From Left: %s should return [1, 1] for sum = 2
        self.assertEqual(sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])
        # First Match From Left REDUX!: %s should return [3, 7] for sum = 10
        self.assertEqual(sum_pairs([4, -2, 3, 3, 4], 8), [4, 4])
        # Duplicates: %s should return [4, 4] for sum = 8
        self.assertEqual(sum_pairs([0, 2, 0], 0), [0, 0])
        # Zeroes: %s should return [0, 0] for sum = 0
        self.assertEqual(sum_pairs([5, 9, 13, -3], 10), [13, -3])
        # Subtraction: %s should return [13, -3] for sum = 10


if __name__ == "__main__":
    unittest.main()
