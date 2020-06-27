# Python solution for 'Reversed Strings' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS and STRINGS.
# Author: Jack Brokenshire
# Date: 27/06/2020

import unittest


def solution(string):
    """
    Complete the solution so that it reverses the string passed into it.
    :param string: a string value.
    :return: the sting reversed.
    """
    return string[::-1]


class TestSolution(unittest.TestCase):
    """Class to test 'solution' function"""

    def test_solution(self):
        self.assertEqual(solution('world'), 'dlrow')
        self.assertEqual(solution('hello'), 'olleh')
        self.assertEqual(solution(''), '')
        self.assertEqual(solution('h'), 'h')


if __name__ == '__main__':
    unittest.main()
