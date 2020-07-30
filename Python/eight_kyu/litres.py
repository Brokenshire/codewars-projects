# Python solution for 'Keep Hydrated!' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, ALGORITHMS, MATHEMATICS, AND NUMBERS.
# Author: Jack Brokenshire
# Date: 30/07/2020

import unittest
import math


def litres(time):
    """
    Finds the amount of water needed to be drunk for x amount of cycling hours.
    :param time: integer value.
    :return:  the number of litres Nathan will drink, rounded to the smallest value.
    """
    return math.trunc(time * 0.5)


class TestLitres(unittest.TestCase):
    """Class to test 'litres' function"""

    def test_litres(self):
        self.assertEqual(litres(2), 1, 'should return 1 litre')
        self.assertEqual(litres(1.4), 0, 'should return 0 litres')
        self.assertEqual(litres(12.3), 6, 'should return 6 litres')
        self.assertEqual(litres(0.82), 0, 'should return 0 litres')
        self.assertEqual(litres(11.8), 5, 'should return 5 litres')
        self.assertEqual(litres(1787), 893, 'should return 893 litres')
        self.assertEqual(litres(0), 0, 'should return 0 litres')


if __name__ == "__main__":
    unittest.main()
