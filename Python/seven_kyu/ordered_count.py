# Python solution for 'Ordered Count of Characters' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 16/06/2020

import unittest
from collections import Counter


def ordered_count(inp):
    """
    Count the number of occurrences of each character.
    :param inp: a string input.
    :return: a list of tuples of each string character and that characters occurrence.
    """
    return sorted(list(Counter(inp).items()), key=lambda x: inp.index(x[0]))


class TestOrderedCount(unittest.TestCase):
    """Class to test 'ordered_count' function"""

    def test_ordered_count(self):
        tests = (
            ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
            ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
        )

        for t in tests:
            inp, exp = t
            self.assertEqual(ordered_count(inp), exp)


if __name__ == '__main__':
    unittest.main()
