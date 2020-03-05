# Python solution for 'Isograms' codewars question.
# Level: 7 kyu
# Tags: Fundamentals and Strings.
# Author: Jack Brokenshire
# Date: 05/03/2020

import unittest


def is_isogram(string):
    """
    An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
    determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
    Ignore letter case.
    :param string: a string value.
    :return: whether or not the input string is an isogram.
    """
    return len(string) == len(set(string.lower()))


class TestIsIsogram(unittest.TestCase):
    """Class to test 'is_isogram' function"""

    def test_is_isogram(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True )
        self.assertEqual(is_isogram("isogram"), True )
        self.assertEqual(is_isogram("aba"), False, "same chars may not be adjacent" )
        self.assertEqual(is_isogram("moOse"), False, "same chars may not be same case" )
        self.assertEqual(is_isogram("isIsogram"), False )
        self.assertEqual(is_isogram(""), True, "an empty string is a valid isogram" )


if __name__ == '__main__':
    unittest.main()
