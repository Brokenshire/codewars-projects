# Python solution for 'Reverse the bits in an integer' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, BITS, and BINARY.
# Author: Jack Brokenshire
# Date: 18/06/2020

import unittest


def reverse_bits(n):
    """
    Reverses the bits in an integer.
    :param n: an integer value.
    :return: finds the integer value of a reversed integer bit.
    """
    return int(bin(n)[::-1][0:-2], 2)


class TestReverseBits(unittest.TestCase):
    """Class to test 'reverse_bits' function"""

    def test_reverse_bits(self):
        self.assertEqual(reverse_bits(417), 267)
        self.assertEqual(reverse_bits(267), 417)
        self.assertEqual(reverse_bits(0), 0)
        self.assertEqual(reverse_bits(2017), 1087)
        self.assertEqual(reverse_bits(1023), 1023)
        self.assertEqual(reverse_bits(1024), 1)


if __name__ == '__main__':
    unittest.main()
