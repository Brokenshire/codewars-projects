# Python solution for 'No Loops 2 - You only need one' codewars question.
# Level: 8 kyu
# Tags: Fundamentals, Booleans, Strings, Numbers, and Arrays
# Author: Jack Brokenshire
# Date: 07/02/2020

import unittest


def check(a, x):
    """
    You will be given an array (a) and a value (x). All you need to do is check whether the provided array contains the
    value, without using a loop. Array can contain numbers or strings. X can be either. Return true if the array contains
    the value, false if not. With strings you will need to account for case.
    :param a: an array of values.
    :param x: a value.
    :return: true if the value 'x' is within the array 'a'.
    """
    return x in a


class TestCheck(unittest.TestCase):
    """Class to test 'check' function"""

    def test_check(self):
        self.assertEqual(check([66, 101], 66), True)
        self.assertEqual(check([80, 117, 115, 104, 45, 85, 112, 115], 45), True)
        self.assertEqual(check(['t', 'e', 's', 't'], 'e'), True)
        self.assertEqual(check(['what', 'a', 'great', 'kata'], 'kat'), False)


if __name__ == '__main__':
    unittest.main()
