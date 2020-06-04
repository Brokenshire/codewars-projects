# Python solution for 'Detect Pangram' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, STRINGS, and DATA STRUCTURES.
# Author: Jack Brokenshire
# Date: 04/06/2020

import unittest
import string


def is_pangram(s):
    """
    Detect whether or not a given string input is a pangram.
    :param s: a string value.
    :return: true if string is a pangram, otherwise false.
    """
    return set(string.ascii_lowercase) <= set(s.lower())


class TestIsPangram(unittest.TestCase):
    """Class to test 'is_pangram' function"""

    def test_is_pangram(self):
        self.assertEquals(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)


if __name__ == '__main__':
    unittest.main()
