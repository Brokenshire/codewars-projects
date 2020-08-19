# Python solution for 'Sum of angles' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, GEOMETRY, ALGEBRA, MATHEMATICS, ALGORITHMS, ARITHMETIC, AND NUMBERS.
# Author: Jack Brokenshire
# Date: 19/08/2020

import unittest


def angle(n):
    """
    Find the total sum of internal angles in an n-sided simple polygon. N will be greater than 2.
    :param n: an integer value.
    :return: sum of internal angle.
    """
    return (n - 2) * 180


class TestAngle(unittest.TestCase):
    """Class to test 'angle' function"""

    def test_angle(self):
        self.assertEqual(angle(3), 180)
        self.assertEqual(angle(4), 360)


if __name__ == "__main__":
    unittest.main()
