# Python solution for 'Basic Mathematical Operations' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, NUMBERS, AND OPERATORS.
# Author: Jack Brokenshire
# Date: 31/07/2020

import unittest


def basic_op(operator, value1, value2):
    """
    Function which does four basic operations.
    :param operator: string/char value.
    :param value1: integer value.
    :param value2: integer value.
    :return: the sum of the equation after using the operator.
    """
    return eval(str(value1) + operator + str(value2))


class TestBasicOp(unittest.TestCase):
    """Class to test 'basic_op' function"""

    def test_basic_op(self):
        self.assertEqual(basic_op('+', 4, 7), 11)
        self.assertEqual(basic_op('-', 15, 18), -3)
        self.assertEqual(basic_op('*', 5, 5), 25)
        self.assertEqual(basic_op('/', 49, 7), 7)


if __name__ == "__main__":
    unittest.main()
