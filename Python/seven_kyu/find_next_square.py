# Python solution for 'Find the next perfect square!' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Numbers, Algebra, Mathematics, and Algorithms.
# Author: Jack Brokenshire
# Date: 05/02/2020

import unittest


def find_next_square(sq):
    """
    Complete the findNextSquare method that finds the next integral perfect square after
    the one passed as a parameter. If the parameter is itself not a perfect square, than -1
    should be returned. You may assume the parameter is positive.
    :param sq: a positive integer.
    :return: the next perfect square after the given one else, not given perfect square return -1.
    """
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


class TestFindNextSquare(unittest.TestCase):
    """Class to test 'find_next_square' function"""

    def test_find_next_square(self):
        self.assertEqual(find_next_square(121), 144)
        self.assertEqual(find_next_square(625), 676)
        self.assertEqual(find_next_square(319225), 320356)
        self.assertEqual(find_next_square(15241383936), 15241630849)
        self.assertEqual(find_next_square(155), -1)
        self.assertEqual(find_next_square(342786627), -1)


if __name__ == '__main__':
    unittest.main()
