# Python solution for 'Area of an arrow' codewars question.
# Level: 7 kyu
# Tags: PUZZLES, MATHEMATICS, ALGORITHMS, AND NUMBERS.
# Author: Jack Brokenshire
# Date: 29/07/2020

import unittest


def arrow_area(a, b):
    """
    An arrow is formed in a rectangle with sides a and b by joining the bottom corners to the midpoint of the top edge
    and the centre of the rectangle.
    :param a: an integer value.
    :param b: an integer value.
    :return: the arrow area of a triangle.
    """
    return (a * b) / 4


class TestArrowArea(unittest.TestCase):
    """Class to test 'arrow_area' function"""

    def test_arrow_area(self):
        self.assertEqual(arrow_area(4, 2), 2)
        self.assertEqual(arrow_area(7, 6), 10.5)
        self.assertEqual(arrow_area(25, 25), 156.25)


if __name__ == "__main__":
    unittest.main()
