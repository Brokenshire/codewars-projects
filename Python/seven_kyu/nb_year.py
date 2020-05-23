# Python solution for 'Growth of a Population' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 23/05/2020

import unittest


def nb_year(p0, percent, aug, p):
    """
    Finds the amount of years required for the population to reach a desired amount.
    :param p0: integer of starting population.
    :param percent: float of percent increase per year.
    :param aug: integer of new inhabitants.
    :param p: integer of desired population.
    :return: the amount of years to reach the population
    """
    if p0 >= p:
        return 0
    else:
        return 1 + nb_year(p0 + (p0 * percent / 100) + aug, percent, aug, p)


class TestNbYear(unittest.TestCase):
    """Class to test 'nb_year' function"""

    def test_nb_year(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)


if __name__ == '__main__':
    unittest.main()
