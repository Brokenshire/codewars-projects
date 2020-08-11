# Python solution for 'Beginner Series #4 Cockroach' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 11/08/2020

import unittest
import math


def cockroach_speed(s):
    """
    Function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).
    :param s: an float value.
    :return: speed in cm per second.
    """
    return math.floor((s / 3600) * 100000)


class TestCockroachSpeed(unittest.TestCase):
    """Class to test 'cockroach_speed' function"""

    def test_cockroach_speed(self):
        self.assertEqual(cockroach_speed(1.08), 30)
        self.assertEqual(cockroach_speed(1.09), 30)
        self.assertEqual(cockroach_speed(0), 0)


if __name__ == "__main__":
    unittest.main()
