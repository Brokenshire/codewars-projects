# Python solution for 'Area or Perimeter' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 03/08/2020

import unittest


def area_or_perimeter(l, w):
    """
    Find either the perimeter of a rectangle or the area of a square.
    :param l: an integer value.
    :param w: an integer value.
    :return: If it is a square, return its area. If it is a rectangle, return its perimeter
    """
    return l * w if l == w else (l + w) * 2


class TestAreaOrPerimeter(unittest.TestCase):
    """Class to test 'area_or_perimeter' function"""

    def test_area_or_perimeter(self):
        self.assertEqual(area_or_perimeter(4, 4), 16)
        self.assertEqual(area_or_perimeter(6, 10), 32)


if __name__ == "__main__":
    unittest.main()
