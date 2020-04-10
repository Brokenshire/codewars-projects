# Python solution for 'Remove String Spaces' codewars question.
# Level: 8 kyu
# Tags: Fundamentals, Strings, and Arrats.
# Author: Jack Brokenshire
# Date: 20/02/2020

import unittest


def no_space(x):
    """
    Simple, remove the spaces from the string, then return the resultant string.
    :param x: A string value input.
    :return: A new string with no spaces.
    """
    return x.replace(" ", "")


class TestNoSpace(unittest.TestCase):
    """Class to test 'no_space' function"""

    def test_no_space(self):
        self.assertEqual(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
        self.assertEqual(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
        self.assertEqual(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
        self.assertEqual(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8')
        self.assertEqual(no_space('8j aam'), '8jaam')


if __name__ == '__main__':
    unittest.main()
