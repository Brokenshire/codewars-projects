# Python solution for 'Find the missing term in an Arithmetic Progression' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, ARITHMETIC, MATHEMATICS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 18/07/2020

import unittest


def find_missing(sequence):
    """
    Receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.
    :param sequence: an array of integers.
    :return: missing integer in a sequence of integers.
    """
    return (sequence[0] + sequence[-1]) * (len(sequence) + 1) / 2 - sum(sequence)


class TestFindMissing(unittest.TestCase):
    """Class to test 'find_missing' function"""

    def test_find_missing(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
        self.assertEqual(find_missing([1, 3, 4, 5, 6, 7, 8, 9]), 2)


if __name__ == '__main__':
    unittest.main()
