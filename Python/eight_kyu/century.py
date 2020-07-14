# Python solution for 'Century From Year' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, NUMBERS, MATHEMATICS, ALGORITHMS, BASIC LANGUAGE FEATURES, AND DATES/TIME.
# Author: Jack Brokenshire
# Date: 14/07/2020

import unittest


def century(year):
    """
    The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to
    and including the year 200, etc.
    :param year: an integer value.
    :return: the current century.
    """
    return (year - 1) // 100 + 1


class TestCentury(unittest.TestCase):
    """Class to test 'century' function"""

    def test_century(self):
        self.asserEqual(century(1705), 18, 'Testing for year 1705')
        self.asserEqual(century(1900), 19, 'Testing for year 1900')
        self.asserEqual(century(1601), 17, 'Testing for year 1601')
        self.asserEqual(century(2000), 20, 'Testing for year 2000')
        self.asserEqual(century(356), 4, 'Testing for year 356')
        self.asserEqual(century(89), 1, 'Testing for year 89')


if __name__ == '__main__':
    unittest.main()
