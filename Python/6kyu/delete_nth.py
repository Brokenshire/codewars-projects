# Python solution for "Delete occurrences of an element if it occurs more than n times" codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, LISTS, and DATA STRUCTURES.
# Author: Jack Brokenshire
# Date: 07/04/2020

import unittest


def delete_nth(order, max_e):
    """
    Given a list lst and a number N, create a new list that contains each number of lst at most N times without
    reordering.
    :param order: an integer array.
    :param max_e: an integer for max number of same element.
    :return: a new list without any number repeated more than the max number amount.
    """
    new_list = []
    for x in order:
        if new_list.count(x) != max_e:
            new_list.append(x)
    return new_list


class TestDeleteNth(unittest.TestCase):
    """Class to test "delete_nth" function"""

    def test_delete_nth(self):
        self.assertEqual(delete_nth([1, 1, 1, 1], 2), [1, 1])
        self.assertEqual(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
        self.assertEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
