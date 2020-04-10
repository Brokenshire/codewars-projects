# Python solution for 'Beginner Series #2 Clock' codewars question.
# Level: 8 kyu
# Tags: Fundamentals.
# Author: Jack Brokenshire
# Date: 28/02/2020

import unittest


def past(h, m, s):
    """
    Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight. Your task is to make 'Past' function which
    returns time converted to milliseconds. Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59
    :param h: hour integer.
    :param m: minute integer.
    :param s: second integer.
    :return: the times converted into milliseconds.
    """
    return (h * 3.6e+6) + (m * 60000) + (s * 1000)


class TestPast(unittest.TestCase):
    """Class to test 'past' function"""

    def test_past(self):
        self.assertEqual(past(0, 1, 1), 61000)
        self.assertEqual(past(1, 1, 1), 3661000)
        self.assertEqual(past(0, 0, 0), 0)
        self.assertEqual(past(1, 0, 1), 3601000)
        self.assertEqual(past(1, 0, 0), 3600000)


if __name__ == '__main__':
    unittest.main()
