# Python solution for 'Abbreviate a Two Word Name' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, STRINGS, and ARRAYS.
# Author: Jack Brokenshire
# Date: 16/05/2020

import unittest


def abbrev_name(name):
    """
    Converts name of two words into initials.
    :param name: a string.
    :return: two capital letters with a dot separating them.
    """
    name = name.split()
    return "{}.{}".format(name[0][0].upper(), name[1][0].upper())


class TestAbbrevName(unittest.TestCase):
    """Class to test 'abbrev_name' function"""

    def test_abbrev_name(self):
        self.assertEqual(abbrev_name("Sam Harris"), "S.H")
        self.assertEqual(abbrev_name("Patrick Feenan"), "P.F")
        self.assertEqual(abbrev_name("Evan Cole"), "E.C")
        self.assertEqual(abbrev_name("P Favuzzi"), "P.F")
        self.assertEqual(abbrev_name("David Mendieta"), "D.M")


if __name__ == '__main__':
    unittest.main()
