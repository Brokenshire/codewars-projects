# Python solution for 'Power of two' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 07/06/2020

import unittest


def power_of_two(x):
    """
    Determines if a given non-negative integer is a power of two.
    :param x: non-negative integer.
    :return: True if x is a power of 2, otherwise False.
    """
    return (x & (x-1) == 0) and x != 0


class TestPowerOfTwo(unittest.TestCase):
    """Class to test 'power_of_two' function"""

    def test_power_of_two(self):
        self.assertEquals(power_of_two(0), False)
        self.assertEquals(power_of_two(1), True)
        self.assertEquals(power_of_two(2), True)
        self.assertEquals(power_of_two(5), False)
        self.assertEquals(power_of_two(6), False)
        self.assertEquals(power_of_two(4096), True)


if __name__ == '__main__':
    unittest.main()
