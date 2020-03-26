# Python solution for "Alternate capitalization" codewars question.
# Level: 7 kyu
# Tags: Fundamentals and Strings.
# Author: Jack Brokenshire
# Date: 26/03/2020

import unittest


def alternate_capitalization(s):
    """
    Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown
    below. Index 0 will be considered even.
    :param s: a string value.
    :return: a list of strings with the first string starting with capitalization alternate and the other lower.
    """
    s = "".join(j if i % 2 else j.upper() for i, j in enumerate(s))
    return [s, s.swapcase()]


class TestAlternateCapitalization(unittest.TestCase):
    """Class to test "alternate_capitalization" function"""

    def test_alternate_capitalization(self):
        self.assertEqual(alternate_capitalization("abcdef"),['AbCdEf', 'aBcDeF'])
        self.assertEqual(alternate_capitalization("codewars"),['CoDeWaRs', 'cOdEwArS'])
        self.assertEqual(alternate_capitalization("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa'])
        self.assertEqual(alternate_capitalization("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS'])


if __name__ == "__main__":
    unittest.main()
