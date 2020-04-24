# Python solution for 'Two Sum' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, ARRAYS, NUMBERS, INTEGERS, ARITHMETIC, MATHEMATICS, and ALGORITHMS.
# Author: Jack Brokenshire
# Date: 24/04/2020

import unittest


def two_sum(numbers, target):
    """
    Finds two values within an array which sum to the target and returns their indices as a list.
    :param numbers: an array of integers.
    :param target: the desired integer number.
    :return: the indices of the two values within the array which sum to the target.
    """
    for i, j in enumerate(numbers):
        for a, b in enumerate(numbers):
            if j + b == target and i != a:
                return [i, a]


class TestTwoSum(unittest.TestCase):
    """Class to test 'two_sum' function"""

    def test_two_sum(self):
        self.assertEqual(sorted(two_sum([1, 2, 3], 4)), [0, 2])
        self.assertEqual(sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])
        self.assertEqual(sorted(two_sum([2, 2, 3], 4)), [0, 1])


if __name__ == '__main__':
    unittest.main()
