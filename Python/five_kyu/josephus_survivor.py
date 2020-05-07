# Python solution for 'Josephus Survivor' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS, MATHEMATICS, NUMBERS, LISTS, DATA STRUCTURES, and ARRAYS.
# Author: Jack Brokenshire
# Date: 08/05/2020

import unittest


def josephus_survivor(n, k):
    """
    Finds the last survivor given an integer of the sum of people and an integer for the amount of steps to take.
    :param n: an integer of people.
    :param k: an integer of steps.
    :return: the lone survivor.
    """
    r = 0
    for x in range(1, n + 1):
        r = (r + k) % x
    return r + 1


class TestJosephusSurvivor(unittest.TestCase):
    """Class to test 'josephus_survivor' function"""

    def test_josephus_survivor(self):
        self.assertEqual(josephus_survivor(7,3),4)
        self.assertEqual(josephus_survivor(11,19),10)
        self.assertEqual(josephus_survivor(1,300),1)
        self.assertEqual(josephus_survivor(14,2),13)
        self.assertEqual(josephus_survivor(100,1),100)


if __name__ == '__main__':
    unittest.main()
