# Python solution for 'Alternate case' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 12/08/2020

import unittest


def alternate_case(s):
    """
    Write function alternateCase which switch every letter in string from upper to lower and from lower to upper.
    :param s: String value.
    :return: Original string but casing reversed.
    """
    return s.swapcase()


class TestAlternateCase(unittest.TestCase):
    """Class to test 'alternate_case' function"""

    def test_alternate_case(self):
        self.assertEqual(alternate_case("ABC"), "abc")
        self.assertEqual(alternate_case(""), "")
        self.assertEqual(alternate_case(" "), " ")
        self.assertEqual(alternate_case("Hello World"), "hELLO wORLD")
        self.assertEqual(alternate_case("cODEwARS"), "CodeWars")
        self.assertEqual(alternate_case("i LIKE MAKING KATAS VERY MUCH"), "I like making katas very much")


if __name__ == "__main__":
    unittest.main()
