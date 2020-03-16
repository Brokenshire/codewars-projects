# Python solution for 'Bit Counting' codewars question.
# Level: 6 kyu
# Tags: Algorithms, Bits, and Binary.
# Author: Jack Brokenshire
# Date: 17/03/2020

import unittest


def count_bits(n):
    """
    Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
    representation of that number. You can guarantee that input is non-negative.
    :param n: a positive integer value.
    :return: the number of bits equal to one in the binary representation of that number.
    """
    return sum(1 for x in bin(n) if x == "1")


class TestCountBits(unittest.TestCase):
    """Class to test 'count_bits' function"""

    def test_count_bits(self):
        self.assertEqual(count_bits(0), 0)
        self.assertEqual(count_bits(4), 1)
        self.assertEqual(count_bits(7), 3)
        self.assertEqual(count_bits(9), 2)
        self.assertEqual(count_bits(10), 2)


if __name__ == '__main__':
    unittest.main()
