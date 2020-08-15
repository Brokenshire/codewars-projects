# Python solution for 'Expressions Matter' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, ALGORITHMS, NUMBERS, AND BASIC LANGUAGE FEATURES.
# Author: Jack Brokenshire
# Date: 15/08/2020

import unittest


def expression_matter(a, b, c):
    """
    Find the maximum value possible.
    :param a: an integer value.
    :param b: an integer value.
    :param c: an integer value.
    :return: the largest number obtained after inserting the following operators and brackets: +, *, ().
    """
    return max(a * (b + c), (a + b) * c, a * b * c, a + b * c, a + b + c)


class TestExpressionMatter(unittest.TestCase):
    """Class to test 'expression_matter' function"""

    def test_expression_matter(self):
        self.assertEqual(expression_matter(5, 1, 3), 20)
        self.assertEqual(expression_matter(3, 5, 7), 105)
        self.assertEqual(expression_matter(5, 6, 1), 35)
        self.assertEqual(expression_matter(1, 6, 1), 8)
        self.assertEqual(expression_matter(2, 6, 1), 14)
        self.assertEqual(expression_matter(6, 7, 1), 48)
        self.assertEqual(expression_matter(2, 10, 3), 60)
        self.assertEqual(expression_matter(1, 8, 3), 27)
        self.assertEqual(expression_matter(9, 7, 2), 126)
        self.assertEqual(expression_matter(1, 1, 10), 20)
        self.assertEqual(expression_matter(9, 1, 1), 18)
        self.assertEqual(expression_matter(10, 5, 6), 300)
        self.assertEqual(expression_matter(1, 10, 1), 12)


if __name__ == "__main__":
    unittest.main()
