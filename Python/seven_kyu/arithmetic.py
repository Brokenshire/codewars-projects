# Python solution for 'Make a function that does arithmetic!' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, OBJECTS, ARITHMETIC, MATHEMATICS, ALGORITHMS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 22/06/2020

import unittest


def arithmetic(a, b, operator):
    """
    Take two integers and perform a math operation on them depending on the operator input.
    :param a: positive integer.
    :param b: positive integer.
    :param operator: string of four operators: "add", "subtract", "divide", "multiply".
    :return: the result of the two numbers having that operator used on them.
    """
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a / b


class TestArithmetic(unittest.TestCase):
    """Class to test 'arithmetic' function"""

    def test_arithmetic(self):
        self.assertEqual(arithmetic(1, 2, "add"), 3, "'add' should return the two numbers added together!")
        self.assertEqual(arithmetic(8, 2, "subtract"), 6, "'subtract' should return a minus b!")
        self.assertEqual(arithmetic(5, 2, "multiply"), 10, "'multiply' should return a multiplied by b!")
        self.assertEqual(arithmetic(8, 2, "divide"), 4, "'divide' should return a divided by b!")


if __name__ == '__main__':
    unittest.main()
