# Python solution for 'Which are in?' codewars question.
# Level: 6 kyu
# Tags: REFACTORING, ARRAYS, SEARCH, ALGORITHMS, LISTS, DATA STRUCTURES, and STRINGS.
# Author: Jack Brokenshire
# Date: 11/06/2020

import unittest
from re import search


def in_array(array1, array2):
    """
    Finds which words within array1 are withing array2 in sorted order.
    :param array1: an array of strings.
    :param array2: an array of strings.
    :return: a sorted array in lexicographical order of the strings of a1 which are substrings of strings of a2.
    """
    result = []
    for i in array1:
        for j in array2:
            if search(i, j) and i not in result:
                result.append(i)
    return sorted(result)


class TestInArray(unittest.TestCase):
    """Class to test 'in_array' function"""

    def test_in_array(self):
        a1 = ["live", "arp", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        self.assertEquals(in_array(a1, a2), r)


if __name__ == '__main__':
    unittest.main()
