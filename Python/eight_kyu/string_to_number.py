# Python solution for 'Convert a String to a Number!' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, PARSING, ALGORITHMS, and STRINGS.
# Author: Jack Brokenshire
# Date: 07/07/2020

import unittest


def string_to_number(s):
    """
    Function that can transform a string into a number
    :param s: an integer in form of a string.
    :return: the string into an integer type.
    """
    return int(s)


class TestStringToNumber(unittest.TestCase):
    """Class to test 'string_to_number' function"""

    def test_string_to_number(self):
        self.assertEqual(string_to_number("1234"), 1234)
        self.assertEqual(string_to_number("605"), 605)
        self.assertEqual(string_to_number("1405"), 1405)
        self.assertEqual(string_to_number("1234"), 1234)


if __name__ == '__main__':
    unittest.main()
