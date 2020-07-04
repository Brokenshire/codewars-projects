# Python solution for 'Counting Array Elements' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS and ARRAYS.
# Author: Jack Brokenshire
# Date: 04/07/2020

import unittest
from collections import Counter


def count(array):
    """
    Write a function that takes an array and counts the number of each unique element present.
    :param array: an array of elements either string or integer.
    :return: number of unique elements in array.
    """
    return Counter(array)


class TestCount(unittest.TestCase):
    """Class to test 'count' function"""

    def test_count(self):
        self.assertEqual(count(['a', 'a', 'b', 'b', 'b']), {'a': 2, 'b': 3})


if __name__ == '__main__':
    unittest.main()
