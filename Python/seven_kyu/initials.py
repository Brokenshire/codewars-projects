# Python solution for 'C.Wars' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, STRINGS, REGULAR EXPRESSIONS, DECLARATIVE PROGRAMMING, and ADVANCED LANGUAGE FEATURES.
# Author: Jack Brokenshire
# Date: 30/06/2020

import unittest


def initials(name):
    """
    Converts a name to initials form.
    :param name: a string of words.
    :return: the string in initials form.
    """
    return ".".join([x[0].upper() for x in name.split()[:-1]] + [name.split()[-1].title()])


class TestInitials(unittest.TestCase):
    """Class to test 'initials' function"""

    def test_initials(self):
        self.assertEqual(initials('code wars'), 'C.Wars')
        self.assertEqual(initials('Barack hussein obama'), 'B.H.Obama')
        self.assertEqual(initials('barack hussein Obama'), 'B.H.Obama')


if __name__ == '__main__':
    unittest.main()
