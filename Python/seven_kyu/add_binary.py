# Python solution for 'Binary Addition' codewars question.
# Level: 7 kyu
# Tags: Fundamentals and Binary.
# Author: Jack Brokenshire
# Date: 16/03/2020

import unittest


def add_binary(a, b):
    """
    Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done
    before, or after the addition. The binary number returned should be a string.
    :param a: an integer value.
    :param b: an integer value.
    :return: the binary value of the sum of a and b.
    """
    return bin(a + b)[2:]


class TestAddBinary(unittest.TestCase):
    """Class to test 'add_binary' function"""

    def test_add_binary(self):
        self.assertEqual(add_binary(1, 1), "10")
        self.assertEqual(add_binary(0, 1), "1")
        self.assertEqual(add_binary(1, 0), "1")
        self.assertEqual(add_binary(2, 2), "100")
        self.assertEqual(add_binary(51, 12), "111111")


if __name__ == '__main__':
    unittest.main()
