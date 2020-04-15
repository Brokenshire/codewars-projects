# Python solution for 'Are they the "same"?' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 15/04/2020

import unittest


def comp(array1, array2):
    """
    Determines if the squares of array1 is the same as array2.
    :param array1: an array of integers.
    :param array2: an array of integers.
    :return: True if the squares of array1 are the same as array2 otherwise, False.
    """
    if array1 is None or array2 is None: return False
    return sorted(array2) == sorted(x * x for x in array1)


class TestSequenceSum(unittest.TestCase):
    """Class to test 'sequence_sum' function"""

    def test_sequence_sum(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
        self.assertEqual(comp(a1, a2), True)


if __name__ == '__main__':
    unittest.main()
