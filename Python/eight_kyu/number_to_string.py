# Python solution for 'Convert a Number to a String!' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, TYPE CASTING, NUMBERS, and STRINGS.
# Author: Jack Brokenshire
# Date: 10/05/2020

import unittest


def number_to_string(num):
    """
    Transform a number into a string.
    :param num: an integer
    :return: the integer as a string.
    """
    return str(num)


class TestNumberToString(unittest.TestCase):
    """Class to test 'number_to_string' function"""

    def test_number_to_string(self):
        self.assertEqual(number_to_string(67), '67')


if __name__ == '__main__':
    unittest.main()
