# Python solution for 'Find the capitals' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, STRINGS, CASE/SWITCH STATEMENTS, CONDITIONAL STATEMENTS, CONTROL FLOW,
# BASIC LANGUAGE FEATURES, ARRAYS, and LOOPS.
# Author: Jack Brokenshire
# Date: 27/04/2020

import unittest


def capitals(word):
    """
    Finds all indexes inside the string where the characters are capital.
    :param word: a string value.
    :return: an ordered list containing the indexes of all capital letters in the string.
    """
    return [i for i, j in enumerate(list(word)) if j == j.capitalize()]


class TestCapitals(unittest.TestCase):
    """Class to test 'capitals' function"""

    def test_capitals(self):
        self.assertEqual(capitals('CodEWaRs'), [0, 3, 4, 6])


if __name__ == '__main__':
    unittest.main()
