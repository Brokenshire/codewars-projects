# Python solution for List Filtering codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Lists, Data Structures, Filtering, and Algorithms
# Author: Jack Brokenshire
# Date: 24/01/2020

import unittest


def filter_list(l):
    """ Return a new list with the strings filtered out."""
    return [x for x in l if type(x) is int]


class TestFindShort(unittest.TestCase):
    """Class to test filter_list function"""

    def test_filter_list(self):
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1, 2])
        self.assertEqual(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])
        self.assertEqual(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])


if __name__ == '__main__':
    unittest.main()
