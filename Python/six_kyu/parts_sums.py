# Python solution for 'Sums of Parts' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, FUNDAMENTALS, and PERFORMANCE.
# Author: Jack Brokenshire
# Date: 17/05/2020

import unittest


def parts_sums(ls):
    """
    Loops through and sums the list removing one element each phase.
    :param ls: a list of integers.
    :return: a new list containing the sum of the old in parts.
    """
    result = [sum(ls)]
    for x in range(len(ls)):
        result.append(result[-1] - ls[x])
    return result


class TestPartsSums(unittest.TestCase):
    """Class to test 'parts_sums' function"""

    def test_parts_sums(self):
        self.assertEqual(parts_sums([]), [0])
        self.assertEqual(parts_sums([0, 1, 3, 6, 10]), [20, 20, 19, 16, 10, 0])
        self.assertEqual(parts_sums([1, 2, 3, 4, 5, 6]), [21, 20, 18, 15, 11, 6, 0])
        self.assertEqual(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]),
                         [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168,
                          2579358, 0])


if __name__ == '__main__':
    unittest.main()
