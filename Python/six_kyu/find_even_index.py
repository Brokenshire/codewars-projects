# Python solution for 'Equal Sides Of An Array' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Algorithms, and Arrays.
# Author: Jack Brokenshire
# Date: 10/03/2020

import unittest


def find_even_index(arr):
    """
    Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the
    sum of the integers to the right of N. If there is no index that would make this happen, return -1.
    :param arr: Array of integers.
    :return: The lowest index N where the side to the left of N is equal to the side to the right of N. If you do
             not find an index that fits these rules, then you will return -1.
    """
    for x in range(len(arr)):
        if sum(arr[0:x]) == sum(arr[x+1:len(arr)]):
            return x
    return -1


class TestFindEvenIndex(unittest.TestCase):
    """Class to test 'find_even_index' function"""

    def test_find_even_index(self):
        self.assertEqual(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
        self.assertEqual(find_even_index([1, 100, 50, -51, 1, 1]), 1, )
        self.assertEqual(find_even_index([1, 2, 3, 4, 5, 6]), -1)
        self.assertEqual(find_even_index([20, 10, 30, 10, 10, 15, 35]), 3)
        self.assertEqual(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)
        self.assertEqual(find_even_index([10, -80, 10, 10, 15, 35, 20]), 6)
        self.assertEqual(find_even_index(list(range(1, 100))), -1)
        self.assertEqual(find_even_index([0, 0, 0, 0, 0]), 0, "Should pick the first index if more cases are valid")
        self.assertEqual(find_even_index([-1, -2, -3, -4, -3, -2, -1]), 3)
        self.assertEqual(find_even_index(list(range(-100, -1))), -1)


if __name__ == '__main__':
    unittest.main()
