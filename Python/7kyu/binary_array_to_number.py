# Python solution for 'Ones and Zeros' codewars question.
# Level: 7 kyu
# Tags: Fundamentals and Arrays.
# Author: Jack Brokenshire
# Date: 27/03/2020

import unittest


def binary_array_to_number(arr):
    """
    Given an array of ones and zeroes, convert the equivalent binary value to an integer.
    :param arr: an array of zeros and ones.
    :return: the binary value of the array.
    """
    return int("".join(str(x) for x in arr), 2)


class TestBinaryArrayToNumber(unittest.TestCase):
    """Class to test 'binary_array_to_number' function"""

    def test_binary_array_to_number(self):
        self.assertEqual(binary_array_to_number([0, 0, 0, 1]), 1)
        self.assertEqual(binary_array_to_number([0, 0, 1, 0]), 2)
        self.assertEqual(binary_array_to_number([0, 1, 0, 1]), 5)
        self.assertEqual(binary_array_to_number([1, 0, 0, 1]), 9)
        self.assertEqual(binary_array_to_number([0, 0, 1, 0]), 2)
        self.assertEqual(binary_array_to_number([0, 1, 1, 0]), 6)
        self.assertEqual(binary_array_to_number([1, 1, 1, 1]), 15)
        self.assertEqual(binary_array_to_number([1, 0, 1, 1]), 11)


if __name__ == '__main__':
    unittest.main()
