# Python solution for 'Vowel Count' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Strings, and Utilities
# Author: Jack Brokenshire
# Date: 09/02/2020

import unittest


def get_count(inputStr):
    """
    Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, and u as vowels for this Kata.
    The input string will only consist of lower case letters and/or spaces.
    :param inputStr: input string value.
    :return: the number (count) of vowels in the given string.
    """
    return sum(1 for i in inputStr if i in ["a", "e", "i", "o", "u"])


class TestGetCount(unittest.TestCase):
    """Class to test 'get_count' function"""

    def test_get_count(self):
        self.assertEqual(get_count("abracadabra"), 5)


if __name__ == '__main__':
    unittest.main()
