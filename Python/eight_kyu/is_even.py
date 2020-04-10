# Python solution for "Is it even?" codewars question.
# Level: 8 kyu
# Tags: Fundamentals and Numbers.
# Author: Jack Brokenshire
# Date: 29/03/2020

import unittest


def is_even(n):
    """
    Determines if the given integer or float input is even.
    :param n: an float or integer value.
    :return: True if the integer is even, otherwise false.
    """
    return n % 2 == 0


class TestIsEven(unittest.TestCase):
    """Class to test "is_even" function"""

    def test_is_even(self):
        self.assertEqual(is_even(0), True)
        self.assertEqual(is_even(0.5), False)
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(-4), True)
        self.assertEqual(is_even(15), False)
        self.assertEqual(is_even(20), True)
        self.assertEqual(is_even(220), True)
        self.assertEqual(is_even(222222221), False)
        self.assertEqual(is_even(500000000), True)


if __name__ == "__main__":
    unittest.main()
