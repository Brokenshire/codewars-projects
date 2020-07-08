# Python solution for 'Functional Addition' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, FUNCTIONAL PROGRAMMING, and DECLARATIVE PROGRAMMING.
# Author: Jack Brokenshire
# Date: 08/07/2020

import unittest


def add(n):
    """
    Adds n to any number.
    :param n: an integer input.
    :return: a function that always adds n to any number.
    """
    return lambda x: x + n


class TestAdd(unittest.TestCase):
    """Class to test 'add' function"""

    def test_add(self):
        add_one = add(1)
        self.assertEqual(add_one(3), 4)

        add_three = add(3)
        self.assertEqual(add_three(3), 6)


if __name__ == '__main__':
    unittest.main()
