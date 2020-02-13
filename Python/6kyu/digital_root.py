# Python solution for 'Sum of Digits / Digital Root' codewars question.
# Level: 6 kyu
# Tags: Algorithms, Mathematics, Numbers, and Arithmetic.
# Author: Jack Brokenshire
# Date: 13/02/2020

import unittest


def digital_root(n):
    """
    A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n.
    If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
    This is only applicable to the natural numbers.
    :param n: A input integer value.
    :return: Adds each digit together in the given number until it reaches a single-digit number.
    """
    while n > 10:
        n = sum([int(x) for x in str(n) if n > 10])
        digital_root(n)
    return n


class TestDigitalRoot(unittest.TestCase):
    """Class to test 'digital_root' function"""

    def test_digital_root(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(456), 6)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)


if __name__ == '__main__':
    unittest.main()
