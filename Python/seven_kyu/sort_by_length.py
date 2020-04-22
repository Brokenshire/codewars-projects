# Python solution for 'Sort array by string length' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, SORTING, ALGORITHMS, and ARRAYS
# Author: Jack Brokenshire
# Date: 22/04/2020

import unittest


def sort_by_length(arr):
    """
    Takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from
    shortest to longest.
    :param arr: an array of strings.
    :return: array sorted from shortest to longest.
    """
    return sorted(arr, key=len)


class TestSortByLength(unittest.TestCase):
    """Class to test 'sort_by_length' function"""

    def test_sort_by_length(self):
        tests = [
            [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
            [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
            [["short", "longer", "longest"], ["longer", "longest", "short"]],
            [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
            [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
            [["a short sentence", "a longer sentence", "the longest sentence"],
             ["a longer sentence", "the longest sentence", "a short sentence"]],
        ]

        for exp, inp in tests:
            self.assertEqual(sort_by_length(inp), exp)


if __name__ == '__main__':
    unittest.main()
