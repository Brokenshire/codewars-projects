# Python solution for 'Short Long Short' codewars question.
# Level: 8 kyu
# Tags: ALGORITHMS.
# Author: Jack Brokenshire
# Date: 19/07/2020

import unittest


def solution(a, b):
    """
    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and
    the longer string on the inside. The strings will not be the same length, but they may be empty ( length 0 ).
    :param a: a string input.
    :param b: a string input.
    :return: the shortest two of the string inputs on the outside of the longer one.
    """
    if len(a) < len(b):
        return a + b + a
    return b + a + b


class TestSolution(unittest.TestCase):
    """Class to test 'solution' function"""

    def test_solution(self):
        self.assertEqual(solution('45', '1'), '1451'),
        self.assertEqual(solution('13', '200'), '1320013'),
        self.assertEqual(solution('Soon', 'Me'), 'MeSoonMe'),
        self.assertEqual(solution('U', 'False'), 'UFalseU')


if __name__ == '__main__':
    unittest.main()
