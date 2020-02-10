# Python solution for 'Get the Middle Character' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, and Strings
# Author: Jack Brokenshire
# Date: 10/02/2020

import unittest


def get_middle(s):
    """
    You are going to be given a word. Your job is to return the middle character of the word. If the word's length is
    odd, return the middle character. If the word's length is even, return the middle 2 characters.
    :param s: A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000
              in some test cases due to an error in the test cases). You do not need to test for this. This
              is only here to tell you that you do not need to worry about your solution timing out.
    :return: The middle character(s) of the word represented as a string.
    """
    return s[int((len(s)-1)/2):int(len(s)/2+1)]


class TestGetMiddle(unittest.TestCase):
    """Class to test 'get_middle' function"""

    def test_get_middle(self):
        self.assertEqual(get_middle("test"), "es")
        self.assertEqual(get_middle("testing"), "t")
        self.assertEqual(get_middle("middle"), "dd")
        self.assertEqual(get_middle("A"), "A")
        self.assertEqual(get_middle("of"), "of")


if __name__ == '__main__':
    unittest.main()
