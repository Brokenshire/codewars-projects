# Python solution for 'Longest Common Subsequence' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS, STRINGS, and SEARCH.
# Author: Jack Brokenshire
# Date: 20/04/2020

import unittest


def lcs(x, y):
    """
    Finds the longest common subsequence of two strings.
    :param x: a string input value.
    :param y: a string input value.
    :return: the longest common subsequence of the two strings.
    """
    matrix = [[0 for x in range(len(y) + 1)] for x in range(len(x) + 1)]
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    char_list = []
    n = len(x)
    m = len(y)
    while n > 0 and m > 0:
        if x[n - 1] == y[m - 1]:
            char_list.append(x[n - 1])
            n -= 1
            m -= 1
        elif matrix[n - 1][m] < matrix[n][m - 1]:
            m -= 1
        else:
            n -= 1
    return "".join(char_list)[::-1]


class TestLCS(unittest.TestCase):
    """Class to test 'lcs' function"""

    def test_lcs(self):
        self.assertEqual(lcs("a", "b"), "")
        self.assertEqual(lcs("abcdef", "abc"), "abc")
        self.assertEqual(lcs("abcdef", "acf"), "acf")
        self.assertEqual(lcs("132535365", "123456789"), "12356")


if __name__ == '__main__':
    unittest.main()
