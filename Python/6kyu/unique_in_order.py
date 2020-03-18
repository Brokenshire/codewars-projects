# Python solution for 'Unique In Order' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Advanced Language Features, and Algorithms.
# Author: Jack Brokenshire
# Date: 18/03/2020

import unittest


def unique_in_order(iterable):
    """
    Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
    elements with the same value next to each other and preserving the original order of elements.
    :param iterable: a string sequence or array of integers.
    :return: the original order of elements without the same value next to each other.
    """
    new_list = []
    for item in iterable:
        if len(new_list) < 1 or not item == new_list[len(new_list) - 1]:
            new_list.append(item)
    return new_list


class TestUniqueInOrder(unittest.TestCase):
    """Class to test 'unique_in_order' function"""

    def test_unique_in_order(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])
        self.assertEqual(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
