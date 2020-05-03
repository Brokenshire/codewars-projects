# Python solution for 'Simple Fun #176: Reverse Letter' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 03/05/2020

import unittest


def reverse_letter(string):
    """
    Given a string str, reverse it omitting all non-alphabetic characters.
    :param string: a string value input.
    :return: the reverse of the string containing only letters.
    """
    return "".join(x for x in string[::-1] if x.isalpha())


class TestReverseLetter(unittest.TestCase):
    """Class to test 'reverse_letter' function"""

    def test_reverse_letter(self):
        self.assertEqual(reverse_letter("krishan"), "nahsirk")
        self.assertEqual(reverse_letter("ultr53o?n"), "nortlu")
        self.assertEqual(reverse_letter("ab23c"), "cba")
        self.assertEqual(reverse_letter("krish21an"), "nahsirk")


if __name__ == '__main__':
    unittest.main()
