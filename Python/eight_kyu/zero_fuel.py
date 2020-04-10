# Python solution for 'Will you make it?' codewars question.
# Level: 8 kyu
# Tags: Fundamentals, Mathematics, Algorithms, and Numbers.
# Author: Jack Brokenshire
# Date: 02/03/2020

import unittest


def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    You were camping with your friends far away from home, but when it's time to go back, you realize that you fuel is
    running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per
    gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to
    get to the pump or not. Function should return true (1 in Prolog) if it is possible and false (0 in Prolog) if not.
    The input values are always positive.
    :param distance_to_pump: an integer value, positive.
    :param mpg: an integer value, positive.
    :param fuel_left: an integer value, positive.
    :return: True if able to make journey to pump on fuel left, otherwise False.
    """
    return distance_to_pump / mpg <= fuel_left


class TestZeroFuel(unittest.TestCase):
    """Class to test 'zero_fuel' function"""

    def test_zero_fuel(self):
        self.assertEqual(zero_fuel(50, 25, 2), True)
        self.assertEquals(zero_fuel(100, 50, 1), False)


if __name__ == '__main__':
    unittest.main()
