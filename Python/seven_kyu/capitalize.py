# Python solution for 'Indexed capitalization' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 28/06/2020

import unittest


def capitalize(s, ind):
    """
    Given a string and an array of integers representing indices, capitalize all letters at the given indices.
    :param s: a string value.
    :param ind: a array of integers representing indices.
    :return: capitalize all letters at the given indices in place.
    """
    return "".join(j.upper() if i in ind else j for i, j in enumerate(s))


class TestCapitalize(unittest.TestCase):
    """Class to test 'capitalize' function"""

    def test_capitalize(self):
        self.assertEqual(capitalize("abcdef", [1, 2, 5]), 'aBCdeF')
        self.assertEqual(capitalize("abcdef", [1, 2, 5, 100]), 'aBCdeF', )
        self.assertEqual(capitalize("codewars", [1, 3, 5, 50]), 'cOdEwArs')
        self.assertEqual(capitalize("abracadabra", [2, 6, 9, 10]), 'abRacaDabRA')
        self.assertEqual(capitalize("codewarriors", [5]), 'codewArriors')


if __name__ == '__main__':
    unittest.main()
