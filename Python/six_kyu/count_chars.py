# Python solution for 'Count characters in your string' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, STRINGS, ASCII, CHARACTER ENCODINGS, and FORMATS.
# Author: Jack Brokenshire
# Date: 16/04/2020

import unittest
from collections import Counter


def count_chars(string):
    """
    The main idea is to count all the occurring characters(UTF-8) in string.
    :param string: a string of characters.
    :return: a dictionary of the amount of times each character appears in given string.
    """
    c = Counter()
    for x in string:
        c[x] += 1
    return c


class TestCountChars(unittest.TestCase):
    """Class to test 'count_chars' function"""

    def test_count_chars(self):
        self.assertEqual(count_chars('aba'), {'a': 2, 'b': 1})
        self.assertEqual(count_chars(''), {})


if __name__ == '__main__':
    unittest.main()
