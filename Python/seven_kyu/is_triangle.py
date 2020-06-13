# Python solution for 'Is this a triangle?' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, NUMBERS, and UTILITIES.
# Author: Jack Brokenshire
# Date: 13/06/2020

import unittest


def is_triangle(a, b, c):
    """
    Determines if 3 integer values can from a triangle.
    :param a: an integer value.
    :param b: an integer value.
    :param c: an integer value.
    :return: true if a triangle can be built with the sides of given length and false in any other case.
    """
    return a + b > c and b + c > a and c + a > b


class TestIsTriangle(unittest.TestCase):
    """Class to test 'is_triangle' function"""

    def test_is_triangle(self):
        self.assertEquals(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
        self.assertEquals(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
        self.assertEquals(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
        self.assertEquals(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
        self.assertEquals(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
        self.assertEquals(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
        self.assertEquals(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
        self.assertEquals(is_triangle(2, 5, 1), False, "didn't work when sides were 2, 5, 1")
        self.assertEquals(is_triangle(4, 2, 3), True, "didn't work when sides were 4, 2, 3")
        self.assertEquals(is_triangle(5, 1, 5), True, "didn't work when sides were 5, 1, 5")
        self.assertEquals(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
        self.assertEquals(is_triangle(-1, 2, 3), False, "didn't work when sides were -1, 2, 3")
        self.assertEquals(is_triangle(1, -2, 3), False, "didn't work when sides were 1, -2, 3")
        self.assertEquals(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")
        self.assertEquals(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")


if __name__ == '__main__':
    unittest.main()
