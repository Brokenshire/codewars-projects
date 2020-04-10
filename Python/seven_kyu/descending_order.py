# Python solution for 'Descending Order' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Functions, Control Flow, and Basic Language Features.
# Author: Jack Brokenshire
# Date: 03/03/2020

import unittest


def descending_order(num):
    """
    Your task is to make a function that can take any non-negative integer as a argument and return it with its digits
    in descending order. Essentially, rearrange the digits to create the highest possible number.
    :param num: an positive integer.
    :return: the integers digits in descending order.
    """
    return int("".join(sorted(str(num))[::-1]))


class TestDescendingOrder(unittest.TestCase):
    """Class to test 'descending_order' function"""

    def test_descending_order(self):
        self.assertEqual(descending_order(0), 0)
        self.assertEqual(descending_order(15), 51)
        self.assertEqual(descending_order(123456789), 987654321)


if __name__ == '__main__':
    unittest.main()
