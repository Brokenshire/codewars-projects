# Python solution for 'String repeat' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS
# Author: Jack Brokenshire
# Date: 11/04/2020

import unittest


def repeat_str(repeat, string):
    """
    Repeats a given string a specified amount of times.
    :param repeat: integer of times to be repeated.
    :param string: the string to be multiplied.
    :return: the string repeated n times.
    """
    return string * repeat


class TestRepeatStr(unittest.TestCase):
    """Class to test repeat_str function"""

    def test_repeat_str(self):
        self.assertEqual(repeat_str(4, 'a'), 'aaaa')
        self.assertEqual(repeat_str(3, 'hello '), 'hello hello hello ')
        self.assertEqual(repeat_str(2, 'abc'), 'abcabc')
        self.assertEqual(repeat_str(6, "I"), "IIIIII")


if __name__ == '__main__':
    unittest.main()
