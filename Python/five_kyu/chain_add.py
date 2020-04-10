# Python solution for "A Chain adding function" codewars question.
# Level: 5 kyu
# Tags: PUZZLES, ARITHMETIC, MATHEMATICS, ALGORITHMS, NUMBERS, FUNCTIONS, CONTROL FLOW, BASIC LANGUAGE FEATURES,
#      FUNDAMENTALS, ADVANCED LANGUAGE FEATURES, FUNCTIONAL PROGRAMMING, and DECLARATIVE PROGRAMMING.
# Author: Jack Brokenshire
# Date: 31/03/2020

import unittest


class CustomInt(int):
    def __call__(self, v):
        return CustomInt(self + v)


def add(v):
    """
    Function that will add numbers together when called in succession.
    :param v: the int to be added.
    :return: the sum of the cain function calls.
    """
    return CustomInt(v)


class TestAdd(unittest.TestCase):
    """Class to test "add" function"""

    def test_add(self):
        self.assertEqual(add(1), 1)
        self.assertEqual(add(1)(2), 3)
        self.assertEqual(add(1)(2)(3), 6)


if __name__ == "__main__":
    unittest.main()
