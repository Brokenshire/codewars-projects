# Python solution for 'Permutations' codewars question.
# Level: 4 kyu
# Tags: ALGORITHMS, PERMUTATIONS, and STRINGS.
# Author: Jack Brokenshire
# Date: 13/05/2020

import unittest
import itertools


def permutations(string):
    """
    Create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all
    letters from the input in all possible orders.
    :param string: a string value.
    :return: all permutations of the string.
    """
    return list("".join(x) for x in set(itertools.permutations(string)))


class TestPermutations(unittest.TestCase):
    """Class to test 'permutations' function"""

    def test_permutations(self):
        self.assertEqual(sorted(permutations('a')), ['a']);
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


if __name__ == '__main__':
    unittest.main()
