# Python solution for 'Snail' codewars question.
# Level: 4 kyu
# Tags: ALGORITHMS and ARRAYS.
# Author: Jack Brokenshire
# Date: 21/04/2020

import unittest


def snail(snail_map):
    """
    Given an n x n array, return the array elements arranged from outermost elements to the middle element,
    traveling clockwise.
    :param snail_map: an array of arrays of integers.
    :return: the path in which the snail takes.
    """
    if not snail_map:
        return snail_map
    res = list()
    n = len(snail_map)
    res += snail_map.pop(0)
    for i in range(1, n - 1):
        res.append(snail_map[i - 1].pop())
    if snail_map:
        res += snail_map.pop()[::-1]
    for i in range(n - 2, 0, -1):
        res.append(snail_map[i - 1].pop(0))
    res += snail(snail_map)
    return res


class TestSnail(unittest.TestCase):
    """Class to test 'snail' function"""

    def test_snail(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(snail(array), expected)

        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(snail(array), expected)


if __name__ == '__main__':
    unittest.main()
