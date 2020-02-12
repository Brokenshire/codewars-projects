# Python solution for 'Remove First and Last Character' codewars question.
# Level: 8 kyu
# Tags: Fundamentals, Basic Language Features, and Strings.
# Author: Jack Brokenshire
# Date: 12/02/2020

import unittest


def remove_char(s):
    """
    It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
    You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
    :param s: original string input.
    :return: a new string with the first and last characters removed.
    """
    return s[1:-1]


class TestRemoveChar(unittest.TestCase):
    """Class to test 'remove_char' function"""

    def test_remove_char(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')
        self.assertEqual(remove_char('person'), 'erso')
        self.assertEqual(remove_char('place'), 'lac')
        self.assertEqual(remove_char('ok'), '')


if __name__ == '__main__':
    unittest.main()
