# Python solution for 'Number Of Occurrences' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, ARRAYS, SEARCH, and ALGORITHMS.
# Author: Jack Brokenshire
# Date: 19/06/2020

import unittest


def number_of_occurrences(element, sample):
    """
    Function that returns the number of occurrences of an element in an array.
    :param element: an integer value.
    :param sample: an array of integers.
    :return: the number of occurrences of an element in an array.
    """
    return sample.count(element)


class TestNumberOfOccurrences(unittest.TestCase):
    """Class to test 'number_of_occurrences' function"""

    def test_number_of_occurrences(self):
        sample = [0, 1, 2, 2, 3]
        self.assertEqual(number_of_occurrences(0, sample), 1)
        self.assertEqual(number_of_occurrences(4, sample), 0)
        self.assertEqual(number_of_occurrences(2, sample), 2)
        self.assertEqual(number_of_occurrences(3, sample), 1)


if __name__ == '__main__':
    unittest.main()
