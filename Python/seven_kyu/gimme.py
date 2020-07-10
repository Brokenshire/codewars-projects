# Python solution for 'Find the middle element' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, and ARRAYS.
# Author: Jack Brokenshire
# Date: 10/07/2020

import unittest


def gimme(input_array):
    """
    Function that when provided with a triplet, returns the index of the numerical element that lies between the
    other two elements.
    :param input_array: an array of integers.
    :return: the index of the middle numerical element in the array.
    """
    return input_array.index(sorted(input_array)[1])


class TestGimme(unittest.TestCase):
    """Class to test 'gimme' function"""

    def test_gimme(self):
        self.assertEqual(gimme([2, 3, 1]), 0, 'Finds the index of middle element')
        self.assertEqual(gimme([5, 10, 14]), 1, 'Finds the index of middle element')


if __name__ == '__main__':
    unittest.main()
